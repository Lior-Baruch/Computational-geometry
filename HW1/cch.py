# Q.1.2.1 - Write a program that sorts a given set P of points into a counterclockwise circular order about an anchor
# point (o in the picture below) that is strictly inside the convex hull of P, e.g., the center of mass of the
# points (their average).
from math import atan2
import numpy as np

atan2_vec = np.vectorize(atan2)


# returns tuple of sorted counterclockwise points and anchor
def sort_counterclockwise_circular(points_unsorted):
    # Convert the points to a numpy array
    points_unsorted = np.array(points_unsorted)

    # Compute the mean of the x and y coordinates of the points
    x_mean = np.mean(points_unsorted[:, 0])
    y_mean = np.mean(points_unsorted[:, 1])
    circular_anchor = (x_mean, y_mean)

    # Sort the points by their polar angle with the (x_mean, y_mean), in
    # counterclockwise order
    sorted_counterclockwise = np.array(
        sorted(points_unsorted, key=lambda point: atan2(point[1] - y_mean, point[0] - x_mean), reverse=True))
    return sorted_counterclockwise, circular_anchor


# Read the filename from the command line
filename = input("Enter the filename for sort_counterclockwise_circular: ")

# Open the file
with open(filename) as f:
    # Read the first line of the file, which contains the number of points
    n = int(f.readline())

    # Read the rest of the file, which contains the coordinates of each point
    points = []
    for line in f:
        x, y = map(float, line.split())
        points.append((x, y))

# Sort the points counterclockwise
points_sorted_circular, anchor = sort_counterclockwise_circular(points)

# Print the sorted points
for curr_point in points_sorted_circular:
    print(curr_point)
print("anchor = {}".format(anchor))
