"""Martian Robots program"""

import sys

def main():
    """
        This is a program for calculating the position of a robot on Mars
        after following a series of instructions
    """

    grid_size_input = input('Enter grid size: ')
    if(not valid_grid_size(grid_size_input)):
        print "Grid size should be a pair of coordinates between 0 0 & 50 50"
        sys.exit()
    grid_size = grid_size_input.split()

    # input validation
    # validate grid size
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

