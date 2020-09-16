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
    raise NotImplementedError()


def jaccard_dist(x, y):
    raise NotImplementedError()


def cosine_sim(x, y):
    raise NotImplementedError()

# Feel free to add more
