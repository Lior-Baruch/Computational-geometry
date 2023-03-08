import sys
import numpy as np
import matplotlib.pyplot as plt


def read_input_file(file_name):
    # Read the input file
    with open(file_name, 'r') as file:
        input_line = file.readline()

    # Split the input line into a list of strings
    input_list = input_line.split()

    # Read the number of lines
    n = int(input_list[0])

    # Read the line coefficients
    line_coefficients = [[float(input_list[i]), float(input_list[i + 1]),
                          float(input_list[i + 2])] for i in range(1, len(input_list), 3)]
    return n, line_coefficients


def compute_bounding_rectangle(line_coefficients):
    n = len(line_coefficients)
    bl_x, bl_y, br_x, br_y, tr_x, tr_y, tl_x, tl_y = None, None, None, None, None, None, None, None

    for i in range(n):
        l1 = line_coefficients[i]
        a1, b1, c1 = l1
        for j in range(i + 1, n):
            l2 = line_coefficients[j]
            a2, b2, c2 = l2

            # Check if the lines are parallel
            if a1 * b2 == a2 * b1:
                continue

            # Compute the intersection point
            x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
            y = (a2 * c1 - a1 * c2) / (a1 * b2 - a2 * b1)

            # Check if the intersection point is inside the rectangle, and update the rectangle
            if bl_x is None or x < bl_x:
                bl_x = x
            if bl_y is None or y < bl_y:
                bl_y = y
            if br_x is None or x > br_x:
                br_x = x
            if br_y is None or y < br_y:
                br_y = y
            if tr_x is None or x > tr_x:
                tr_x = x
            if tr_y is None or y > tr_y:
                tr_y = y
            if tl_x is None or x < tl_x:
                tl_x = x
            if tl_y is None or y > tl_y:
                tl_y = y

    # Check if the rectangle is unbounded
    if bl_x is None or bl_y is None or br_x is None or br_y is None or tr_x is None or tr_y is None or tl_x is None or tl_y is None:
        return None

    # Return the bounding rectangle
    return bl_x, bl_y, br_x, br_y, tr_x, tr_y, tl_x, tl_y


def plot_lines(line_coefficients):
    for i in range(len(line_coefficients)):
        l = line_coefficients[i]
        a, b, c = l
        x = np.linspace(-100, 100, 1000)
        y = (-c - a * x) / b
        plt.plot(x, y, label=f'line {i}')
    plt.legend()
    plt.show()


def plot_bounding_rectangle(bounding_rectangle):
    bl_x, bl_y, br_x, br_y, tr_x, tr_y, tl_x, tl_y = bounding_rectangle
    plt.plot([bl_x, br_x], [bl_y, br_y], label='bottom')
    plt.plot([br_x, tr_x], [br_y, tr_y], label='right')
    plt.plot([tr_x, tl_x], [tr_y, tl_y], label='top')
    plt.plot([tl_x, bl_x], [tl_y, bl_y], label='left')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    file_name = 'lines.txt'
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    n, line_coefficients = read_input_file(file_name)
    bounding_rectangle = compute_bounding_rectangle(line_coefficients)
    if bounding_rectangle is None:
        print('The rectangle is unbounded!')
    else:
        print(f'Bounding rectangle: {bounding_rectangle}')
        plot_lines(line_coefficients)
        plot_bounding_rectangle(bounding_rectangle)
