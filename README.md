# Robot-Terrain-Program

## Problem Description

A robot listens to inputs and makes movements based on the input. Such an input can only be a two-letter input. For e.g N4, E3, S1, W2. The first character of the input refers to the first letter of the directions- North, East, West and South. The second character of the input refers to the number of steps to take in the direction. Write a program with appropriate unit test cases in a language that you are comfortable to:

1. Create multiple robots.
2. Associate each robot with a unique number.
3. Move a selected robot in terrain based on the input. If there is already a robot at the destination cell, the robot should stop in the previous cell.
4. Display the current location of the selected robot in the terrain.

Assume that:

1. The terrain is represented as a grid/matrix of rows and columns, where each cell corresponds to a step to be taken by the robot, and
2. A robot always starts at the first cell of the grid.
3. The terrain doesn't need to be visually represented.


### Steps to run the program

1. Clone the repositry.
2. First, install pytest if you haven't already:
   `pip install pytest`
3. To Run the test file, use the following command in the terminal :
    `pytest test_robot.py -v`
