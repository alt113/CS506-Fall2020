from collections import defaultdict
from math import inf, pow
from .sim import euclidean_dist

import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    # get the total number of points
    num_of_input_points = len(points)

    # get the total number of dimensions per point
    num_of_input_point_dimensions = len(points[0])

    # list containing the new center point
    list_of_center_point_dimensions = []

    for i in range(num_of_input_point_dimensions):
        sum_of_dimension = 0
        for j in range(num_of_input_points):
            sum_of_dimension += points[j][i]
        sum_of_dimension /= num_of_input_points
        list_of_center_point_dimensions.append(sum_of_dimension)

    return list_of_center_point_dimensions


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    # get the number of clusters 'k'
    number_of_clusters = max(assignments)

    # list of 'k' cluster centers
    all_cluster_centers = []

    for cluster_index in range(number_of_clusters):
        tmp = []
        for i in range(len(assignments)):
            if assignments[i] == cluster_index+1:
                tmp.append(dataset[i])
        all_cluster_centers.append(point_avg(tmp))

    return all_cluster_centers


def assign_points(data_points, centers):
    """
        Assign each element in data_points to a cluster.
        Each cluster is identified by its center.

        Returns a list of data point assignments
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
        Returns the Euclidean distance between a and b
    """
    return euclidean_dist(a, b)


def distance_squared(a, b):
    """
        Returns the squared distance between a and b
    """
    return pow(distance(a, b), 2.0)


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    return random.choices(dataset, k=k)


def cost_function(clustering):
    """
        Calculate the cost of the current clustering

        *Note: clustering is a dictionary of the following form:
                key = clustering assignment index
                value = list of points
    """
    # work around to be able to use dictionary methods
    assert isinstance(clustering, dict )

    list_of_squared_distances = []

    for list_of_cluster_points in clustering.values():
        cluster_avg = point_avg(list_of_cluster_points)
        tmp_sum = 0
        for point in list_of_cluster_points:
            tmp_sum += distance_squared(point, cluster_avg)
            list_of_squared_distances.append(tmp_sum)

    return sum(list_of_squared_distances)


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    # select a random point from the dataset as a cluster mean
    random_initial_point = random.choice(dataset)

    # dictionary to hold my minimum distance values for points
    point_cluster_min_distances = dict()

    # get the minimum distance between each dataset sample and
    # the list of random_set_of_k_points
    for data_sample in dataset:
        minimum_distance_squared = inf
        if distance_squared(data_sample, random_initial_point) < minimum_distance_squared:
            minimum_distance_squared = distance_squared(data_sample, random_initial_point)
        point_cluster_min_distances[data_sample] = minimum_distance_squared

    denominator_sum = sum(point_cluster_min_distances.values())

    weights = [p/denominator_sum for p in point_cluster_min_distances.values()]

    return random.choices(dataset, weights=weights, k=k-1)


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)

# --
