import math
import sys


def read_polygon(filename):
    with open(filename, "r") as f:
        data = f.readline().split()
        n = int(data[0])
        points = []
        for i in range(n):
            x, y = map(float, data[i * 2 + 1:i * 2 + 3])
            points.append((x, y))
    return points


def compute_height(polygon):
    min_y = float("inf")
    max_y = float("-inf")
    for vertex in polygon:
        if vertex[1] < min_y:
            min_y = vertex[1]
        if vertex[1] > max_y:
            max_y = vertex[1]
    return max_y - min_y


def rotate(point, angle):
    x, y = point
    return x * math.cos(angle) - y * math.sin(angle), x * math.sin(angle) + y * math.cos(angle)


def compute_width(polygon):
    min_x = min(vertex[0] for vertex in polygon)
    max_x = max(vertex[0] for vertex in polygon)
    return max_x - min_x


def find_direction(polygon, width, angle_step = 0.01):
    # Set the initial direction to the up vector (0, 1)
    direction = (0, 1)
    min_height = float("inf")
    min_direction = None

    # Rotate the polygon by small angles and compute the height until we find the minimum
    angle = 0  # start with a small rotation angle
    while angle <= 2 * math.pi:
        rotated_direction = rotate(direction, angle)
        rotated_polygon = [rotate(vertex, angle) for vertex in polygon]
        curr_width = compute_width(rotated_polygon)
        if curr_width <= width:
            height = compute_height(rotated_polygon)
            if height < min_height:
                min_height = height
                min_direction = rotated_direction
        angle += angle_step  # increase the rotation angle

    return min_direction


if __name__ == "__main__":
    # Read the width of the printer from the command line arguments
    if len(sys.argv) < 2:
        print("Usage: python finddir.py <width> [<input_file>]")
        sys.exit(1)
    width = float(sys.argv[1])

    # Read the input polygon.txt from the file
    if len(sys.argv) >= 3:
        input_file = sys.argv[2]
    else:
        input_file = "polygon.txt"

    # Read the polygon from the file
    polygon = read_polygon(input_file)

    # Find the direction that minimizes the height of the polygon.txt
    direction = find_direction(polygon, width)
    if direction:
        print("Direction {} {}".format(direction[0], direction[1]))
    else:
        print("The polygon cannot be printed, because it is too wide")
