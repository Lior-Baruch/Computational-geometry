import math
import sys
from collections import defaultdict

from matplotlib import pyplot as plt


def read_segments(filename):
    with open(filename, 'r') as file:
        data = file.readline().split()
        n = int(data[0])
        segments = []
        points = []
        for i in range(n):
            x1, y1, x2, y2 = map(float, (data[1 + i * 4], data[2 + i * 4], data[3 + i * 4], data[4 + i * 4]))
            segments.append((x1, y1, x2, y2))

        for i in range(4 * n + 1, len(data), 2):
            x1, y1 = float(data[i]), float(data[i + 1])
            points.append((x1, y1))
        return segments, points


# Plot the segments and the line
def plot_seg_line(segments, line=None):
    # Plot the segments
    for segment in segments:
        x1, y1, x2, y2 = segment
        plt.plot([x1, x2], [y1, y2], 'k-')
    # Plot the line
    if line:
        x1, y1, x2, y2 = line
        plt.plot([x1, x2], [y1, y2], 'r-')
    plt.show()


# Function to check if point (x, y) is contained in line ax + by = c
def is_on_line(a, b, c, x, y, epsilon=1e-6):  # epsilon is the tolerance, because of floating point arithmetic
    if abs(a * x + b * y - c) < epsilon:
        return True
    return False


# Function to divide points into sqrt(n) groups
def divide_points(points):
    groups = defaultdict(list)
    sqrt_n = int(math.sqrt(len(points)))
    for i, point in enumerate(points):
        groups[i // sqrt_n].append(point)
    return groups


# Function to check if any point in a group is contained in any line
def check_group(lines, group):
    for line in lines:
        x1, y1, x2, y2 = line
        a, b, c = y1 - y2, x2 - x1, x1 * y2 - x2 * y1
        for point in group:
            if is_on_line(a, b, c, point[0], point[1]):
                return point, a, b, c
    return None


# Main function to check if any point is contained in any line
def iscont(lines, points):
    groups = divide_points(points)
    for group in groups.values():
        point_line = check_group(lines, group)
        if point_line is not None:
            return point_line
    return None


# test
if __name__ == '__main__':
    file_name = 'line_points.txt'  # Default file name
    if len(sys.argv) > 1:  # Read the file name from the command line
        file_name = sys.argv[1]

    segments, points = read_segments(filename=file_name)
    # print(segments)
    # print(points)
    point_line = iscont(segments, points)
    if point_line is not None:
        point, a, b, c = point_line
        x, y = point
        print(x, y, a, b, c)
    else:
        print('None of the lines contain any point!')
