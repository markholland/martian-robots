"""Martian Robots program"""

import sys
import re

def main():
    """
        This is a program for calculating the position of a robot on Mars
        after following a series of instructions
    """

    grid_size = raw_input('Enter grid size: ')
    if(not valid_grid_size(grid_size)):
        print 'Grid size should be a pair of coordinates between 0 0 & 50 50'
        sys.exit()
    grid_size = grid_size.split()
    grid = [[0 for i in range(int(grid_size[0]))] for j in range(int(grid_size[1]))]

    while True:
        initial_pos = raw_input('Provide the initial position and orientation of a robot: ')
        if(not valid_initial_pos(initial_pos)):
            print 'Initial position should be a coordinate and orientation i.e. 22 3 E'
            continue
        initial_pos = get_initial_pos_as_dict(initial_pos)

        instructions = raw_input('Provide the series of instructions for the robot: ')
        if(not valid_list_of_instructions(instructions)):
            print 'A valid instruction contains turns L or R and movements F with a limit of 100'
            continue

def get_position_change(orientation):
    if orientation == 'N':
        delta = {'x': 0, 'y': 1}
    if orientation == 'S':
        delta = {'x': 0, 'y': -1}
    if orientation == 'E':
        delta = {'x': 1, 'y': 0}
    if orientation == 'W':
        delta = {'x': -1, 'y': 0}
    return delta  

def get_new_orientation_after_left_turn(orientation):
    if orientation == 'N':
        return 'W'
    if orientation == 'E':
        return 'N'
    if orientation == 'S':
        return 'E'
    if orientation == 'W':
        return 'S'

def get_new_orientation_after_right_turn(orientation):
    if orientation == 'N':
        return 'E'
    if orientation == 'E':
        return 'S'
    if orientation == 'S':
        return 'W'
    if orientation == 'W':
        return 'N'

def valid_grid_size(grid_size):
    grid_size = grid_size.split()
    if len(grid_size) != 2:
        return False
    for coordinate in grid_size:
        if not coordinate.isdigit():
            return False
        if int(coordinate) > 50:
            return False
    return True

def valid_initial_pos(initial_pos):
    initial_pos = initial_pos.split()
    if len(initial_pos) != 3:
        return False

    x_coord = int(initial_pos[0])
    y_coord = int(initial_pos[1])
    orientation = initial_pos[2]

    if x_coord > 50 or y_coord > 50:
        return False
    if not valid_orientation(orientation):
        return False

    return True

def valid_orientation(orientation):
    return re.search(r'[NESW]', orientation)

def valid_list_of_instructions(instructions):
    instructions = instructions.split()[0]
    if not len(instructions) < 100:
        return False
    if not re.search(r'^[FLR]+$', instructions):
        return False
    return True

def get_initial_pos_as_dict(initial_pos):
    return {'x': initial_pos[0], 'y': initial_pos[1], 'orientation': initial_pos[2]}

if __name__ == '__main__':
    main()