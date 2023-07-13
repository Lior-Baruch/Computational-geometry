# Computational Geometry Course Assignments

This repository contains solutions for three assignments from a Computational Geometry course taught by Efi Fogel at Reichman University in Fall 2023. Each assignment, named as `assignX` where `X` is the assignment number, is included in its own directory.

## Getting Started

1. Clone this repository.
2. Navigate to the respective assignment directory for the source files, documentation, and instructions for running the programs.
3. Depending on the assignment, you might need Python or a C++ compiler, and possibly additional libraries such as NumPy, Matplotlib, CGAL, and CMake.

## Assignments

### Assignment 1 (`assign1`)

This assignment includes solutions to tasks related to sorting points using the convex hull function and sorting a set of integers using a function that computes the convex hull of a set of points. The Python scripts for these tasks are `cch.py` and `chs.py`, respectively.

### Assignment 2 (`assign2`)

This assignment contains a Python script `finddir.py` in the `finddir` subdirectory, which reads a polygon from a file and finds the direction that minimizes the height of the polygon.

### Assignment 3 (`assign3`)

This assignment includes solutions to several computational geometry problems, implemented in Python scripts in various subdirectories:

- `ex1_stabber` contains `stabber.py`: This script reads a set of segments from a file and checks if there exists a line that stabs all the segments.
- `ex3_bblines` contains `bblines.py`: This script reads a set of lines from a file and computes the axis-parallel bounding rectangle of their intersection points.
- `ex4_iscont` contains `iscont.py`: This script reads a set of lines and points from a file and checks if any point is contained in any line.

## Running the Programs

To run the programs, navigate to the root directory of the respective assignment and follow the instructions provided in the respective README files.

## Dependencies

The programs may rely on various libraries, including NumPy, Matplotlib, CGAL, and CMake, depending on the assignment.

## Contributors

The solutions were implemented by Lior Baruch.

## License

This project is licensed under the terms of the MIT license. Please refer to the LICENSE file for more information.
