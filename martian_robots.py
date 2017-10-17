"""Martian Robots program"""

import sys
import re

def main():
    """
        This is a program for calculating the position of robots on Mars
        after following a series of instructions
    """

    grid_size = raw_input('Enter grid size: ')
    if not valid_grid_size(grid_size):
        print 'Grid size should be a pair of coordinates between 0 0 & 50 50'
        sys.exit()
    grid_size = grid_size.split()
    grid = [[0 for i in range(int(grid_size[0]) + 1)] for j in range(int(grid_size[1]) + 1)]

    while True:
        initial_pos = raw_input('Provide the initial position and orientation of a robot: ')
        if not valid_initial_pos(initial_pos):
            print 'Initial position should be a coordinate and orientation i.e. 22 3 E'
            continue
        initial_pos = get_initial_pos_as_dict(initial_pos)

        instructions = raw_input('Provide the series of instructions for the robot: ')
        if not valid_list_of_instructions(instructions):
            print 'A valid instruction contains turns L or R and movements F with a limit of 100'
            continue
        final_pos = get_final_position(grid, initial_pos, instructions)
        print build_output(final_pos)

def build_output(pos):
    output = ""
    output += str(pos['x']) + ' ' + str(pos['y']) + ' ' + pos['orientation']
    if pos['over_edge'] is True:
        output += ' ' + 'LOST'
    return output

def get_final_position(grid, initial_pos, instructions):
    current_pos = {
        'x': int(initial_pos['x']),
        'y': int(initial_pos['y']),
        'orientation': initial_pos['orientation'],
        'over_edge': False
    }

    for instr in instructions:
        if instr == 'F':
            current_pos = get_new_position(grid, current_pos)
            if current_pos['over_edge'] is True:
                break
        if instr == 'L':
            current_pos['orientation'] = get_new_orientation_after_left_turn(current_pos['orientation'])
        if instr == 'R':
            current_pos['orientation'] = get_new_orientation_after_right_turn(current_pos['orientation'])

    return current_pos

def get_new_position(grid, current_pos):
    delta = get_position_change(current_pos['orientation'])
    new_pos = {
        'x': int(current_pos['x'] + delta['x']),
        'y': int(current_pos['y'] + delta['y']),
        'orientation': current_pos['orientation'],
        'over_edge': False
    }
    if picks_up_scent(grid, current_pos):
        new_pos = current_pos
    elif over_the_edge(grid, new_pos):
        grid[current_pos['x']][current_pos['y']] = current_pos['orientation']
        new_pos['over_edge'] = True
    return new_pos

def over_the_edge(grid, pos):
    if int(pos['x']) > (len(grid) - 1) or int(pos['y']) > (len(grid[0]) - 1):
        return True
    return False

def picks_up_scent(grid, current_pos):
    return grid[current_pos['x']][current_pos['y']] == current_pos['orientation']

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