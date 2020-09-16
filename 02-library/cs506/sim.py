def euclidean_dist(x, y):
    """
        Compute the Euclidean Distance between two variables based on the
        following equation (source: https://en.wikipedia.org/wiki/Euclidean_distance#n_dimensions)

        d(x,y) = sqrt( summation(p_i - q_i)^2 ) for all i

        *Note: the answer is rounded up to 2 decimal points
    """
    # store the sum of squared differences
    sum_squared_diff = 0
    for x_i, y_i in zip(x, y):
        sum_squared_diff += pow((x_i - y_i), 2)
    return round(pow(sum_squared_diff, 0.5), 2)


def manhattan_dist(x, y):
    """
        Compute the Manhattan Distance between two variables based on the
        following equation (source: https://en.wikipedia.org/wiki/Taxicab_geometry)

        d(x,y) = summation( abs(p_i - q_i) ) for all i

        *Note: the answer is rounded up to 2 decimal points
    """
    sum_abs_diff = 0
    for x_i, y_i in zip(x, y):
        sum_abs_diff += abs(x_i - y_i)
    return round(sum_abs_diff, 2)


def jaccard_dist(x, y):
    """
        Computes the Jaccard distance between two variables based on the
        following equation (source: https://en.wikipedia.org/wiki/Jaccard_index)

        d(x,y) = 1 - J(x,y) = 1 - ( | intersection(x,y) | / |x| + |y| - | intersection(x,y) | )

        where: |var| = size

        *Note: the answer is rounded up to 2 decimal points
    """
    try:
        return round((list_union_size(x, y) - list_intersection_size(x, y))/list_union_size(x, y), 2)
    except ZeroDivisionError:
        return 0


def cosine_sim(x, y):
    """
        Compute the Cosine similarity between two variables based on the
        following equation (source: https://en.wikipedia.org/wiki/Cosine_similarity)

        cos(x,y) = X.Y / ||X|| ||Y||

        *Note: the answer is rounded up to 2 decimal points
    """
    try:
        return round(list_dot_product(x, y)/(list_magnitude(x) * list_magnitude(y)), 2)
    except ZeroDivisionError:
        return 0

# Feel free to add more


def list_intersection_size(list1, list2):
    """
        Compute the number of elements in the intersection between list1 and list2
    """
    return len(list(set(list1) & set(list2)))


def list_union_size(list1, list2):
    """
        Compute the number of elements in the union between list1 and list2
    """
    return len(list(set(list1) | set(list2)))


def list_dot_product(list1, list2):
    """
        Compute the dot product of two lists
    """
    result = 0
    for x_i, y_i in zip(list1, list2):
        result += x_i*y_i
    return result


def list_magnitude(list1):
    """
        Compute the magnitude of a list
    """
    result = 0
    for elem in list1:
        result += pow(elem, 2)
    return pow(result, 0.5)
