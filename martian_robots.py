"""Martian Robots program"""

import sys
import re

def main():
    """
        This is a program for calculating the position of a robot on Mars
        after following a series of instructions
    """

    grid_size_input = raw_input('Enter grid size: ')
    if(not valid_grid_size(grid_size_input)):
        print 'Grid size should be a pair of coordinates between 0 0 & 50 50'
        sys.exit()
    grid_size = grid_size_input.split()

    while True:
        initial_pos_input = raw_input('Provide the initial position and orientation of a robot: ')
        if(not valid_initial_pos(initial_pos_input)):
            print 'Initial position should be a coordinate and orientation i.e. 22 3 E'
            continue

    # loop robots
        # validate starting position
        # validate starting orientation
        # validate instruction length
        # validate instruction content
        # calc final position
            # mark scent
            # detect scent
        # print output
            # LOST if left grid
    # end loop
    # end

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

if __name__ == '__main__':
    main()