import matplotlib.pyplot as plt


def draw_data(circle_1, circle_2):
    """
    Function draws 2 circles using matplotlib library.

    :param circle_1: (list): parameters of a circle in format [center x-coordinate, center y-coordinate, circle radius]
    :param circle_2: (list): parameters of a circle in format [center x-coordinate, center y-coordinate, circle radius]
    :return: None
    """
    figure, axes = plt.subplots()

    first_circle = plt.Circle(
        tuple(circle_1[0:2]),
        circle_1[2],
    )
    second_circle = plt.Circle(
        tuple(circle_2[0:2]),
        circle_2[2],
    )

    axes.add_artist(first_circle)
    axes.add_artist(second_circle)

    axes.set_xlim([-10, 10])
    axes.set_ylim([-10, 10])

    axes.set_aspect(1)
    plt.show()
