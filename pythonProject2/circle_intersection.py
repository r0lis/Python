from circles import stats as cs
from circles import draw


def main(circle_1, circle_2):
    """
    Driver function that uses module 'circles' for an identification of possible intersection between two circles

    :param circle_1: (list): parameters of a circle in format [center x-coordinate, center y-coordinate, circle radius]
    :param circle_2: (list): parameters of a circle in format [center x-coordinate, center y-coordinate, circle radius]
    :return: None
    """
    has_intersection, count = cs.has_intersection(circle_1, circle_2)

    if has_intersection:
        print(f'Kruznice maji {count} pruniku.')
    else:
        print(f'Kruznice nemaji zadny prunik.')

    # Vykresleni dat
    draw.draw_data(circle_1, circle_2)


if __name__ == '__main__':

    c1_test = [0, 0, 0.5]
    c2_test = [0, 1, 0.2]

    main(c1_test, c2_test)
