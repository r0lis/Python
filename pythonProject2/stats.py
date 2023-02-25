from math import sqrt


def euclid_distance(x1, y1, x2, y2):
    """
    Function returns Euclidean distance of 2 point in 2D space.

    :param x1: (float) x-coordinate of the 1st point
    :param y1: (float) y-coordinate of the 1st point
    :param x2: (float) x-coordinate of the 2nd point
    :param y2: (float) y-coordinate of the 2nd point
    :return: (float) Euclidean distance
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def radius_sum(r1, r2):
    """
    Function returns sum of 2 radii

    :param r1: (float) radius 1
    :param r2: (float) radius 2
    :return: (float) sum of radii
    """
    return r1 + r2


def has_intersection(circle_1, circle_2):
    """
    Function indentifies whether two circles has intersection or not.

    :param circle_1: (list): parameters of a circle in format [center x-coordinate, center y-coordinate, circle radius]
    :param circle_2: (list): parameters of a circle in format [center x-coordinate, center y-coordinate, circle radius]
    :return: (bool, int): True if circles has intersection and their count, False otherwise
    """
    x1, y1, r1 = circle_1
    x2, y2, r2 = circle_2

    r_sum = radius_sum(r1, r2)
    center_distance = euclid_distance(x1, y1, x2, y2)

    if r_sum < center_distance:
        return False, 0
    else:
        if r_sum == center_distance:
            return True, 1
        else:
            return True, 2


assert radius_sum(1, 2) == 3
assert radius_sum(2, 3) == 5
assert euclid_distance(x1=1, y1=0, x2=2, y2=0) == 1
assert euclid_distance(x1=-2, y1=2, x2=2, y2=2) == 4
assert has_intersection(circle_1=[0, 0, 2], circle_2=[0, 3, 1]) == (True, 1)
assert has_intersection(circle_1=[0, 0, 2], circle_2=[0, 3, 2]) == (True, 2)
assert has_intersection(circle_1=[2, -1, 1], circle_2=[1.2, 5, 3]) == (False, 0)
