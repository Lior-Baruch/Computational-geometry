import numpy as np
from scipy.spatial import ConvexHull


# Q.1.1 - Write a program that sorts a given set on n integers utilizing a function that computes the
# convex hull of a set of points in the plane.
def sort_using_convex_hull(int_arr):
    # Create a set of points using the integers as coordinates
    points = np.array([[number, number * number] for number in int_arr])

    # Compute the convex hull of the points
    hull = ConvexHull(points)

    # Sort the original set of numbers using the vertices of the convex hull
    sorted_arr = [points[vertex, 0] for vertex in hull.vertices]
    min_index = np.argmin(sorted_arr)
    sorted_arr = np.roll(sorted_arr, -min_index)
    return sorted_arr


# Read the filename from the command line
filename = input("Enter the filename for sort_using_convex_hull: ")

# Open the file
with open(filename) as f:
    # Read the numbers from the file
    numbers = [int(line) for line in f]

sorted_numbers = sort_using_convex_hull(numbers)

# Print the sorted numbers
for number in sorted_numbers:
    print(number)

