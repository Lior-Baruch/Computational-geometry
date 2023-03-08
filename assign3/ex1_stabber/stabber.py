import sys


def open_file(filename):
    with open(filename, 'r') as f:
        input = (f.readline().split(' '))
        input = [float(i) for i in input]
        input.remove(input[0])
        segments = []
        for i in range(0, len(input), 4):
            x1, y1, x2, y2 = input[i], input[i + 1], input[i + 2], input[i + 3]
            segments.append([x1, y1, x2, y2])
        return segments


def find_stabber_line(segments):
    # Initialize the line with the first segment
    a, b, c = find_line_equation(segments[0])
    for segment in segments[1:]:
        # Find the equation of the current segment
        a1, b1, c1 = find_line_equation(segment)
        # Find the intersection point of the current segment and the stabber line
        intersection = find_intersection(a, b, c, a1, b1, c1)
        if intersection is None:
            return None
        x, y = intersection
        # Update the stabber line with the intersection point
        a, b, c = find_line_equation((x, y, x, y))
    return a, b, c


def find_line_equation(segment):
    x1, y1, x2, y2 = segment
    a = y2 - y1
    b = x1 - x2
    c = (x2 * y1) - (x1 * y2)
    return (a, b, c)


def find_intersection(a1, b1, c1, a2, b2, c2):
    determinant = (a1 * b2) - (a2 * b1)
    if determinant == 0:
        # Lines are parallel
        return None
    x = ((b2 * c1) - (b1 * c2)) / determinant
    y = ((a1 * c2) - (a2 * c1)) / determinant
    return (x, y)


if __name__ == '__main__':
    file_name = 'segments.txt'
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    segments = open_file(file_name)
    line = find_stabber_line(segments)
    if line is None:
        print('A stabber does not exist!')
    else:
        print(line)
