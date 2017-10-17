""" Unit tests for Martian Robots program"""
import unittest

from martian_robots import valid_grid_size, valid_initial_pos, valid_orientation, valid_list_of_instructions

class TestInputValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_validate_grid_size(self):
        grid_size = '1 2'
        self.assertTrue(valid_grid_size(grid_size))

        grid_size = '50 50'
        self.assertTrue(valid_grid_size(grid_size))

        grid_size = '50 51'
        self.assertFalse(valid_grid_size(grid_size))

        grid_size = '51 50'
        self.assertFalse(valid_grid_size(grid_size))

        grid_size = '0 -1'
        self.assertFalse(valid_grid_size(grid_size))

        grid_size = '1'
        self.assertFalse(valid_grid_size(grid_size))

        grid_size = '1 2 3'
        self.assertFalse(valid_grid_size(grid_size))

        grid_size = 'a'
        self.assertFalse(valid_grid_size(grid_size))

        grid_size = '1,3'
        self.assertFalse(valid_grid_size(grid_size))

    def test_validate_starting_position(self):
        initial_pos = '1 2 E'
        self.assertTrue(valid_initial_pos(initial_pos))

        initial_pos = '50 50 W'
        self.assertTrue(valid_initial_pos(initial_pos))
        
        initial_pos = '1 2 D'
        self.assertFalse(valid_initial_pos(initial_pos))

        initial_pos = '51 50 N'
        self.assertFalse(valid_initial_pos(initial_pos))

        initial_pos = '1 2'
        self.assertFalse(valid_initial_pos(initial_pos))

        initial_pos = 'E'
        self.assertFalse(valid_initial_pos(initial_pos))

    def test_validate_orientation(self):
        orientation = 'E'
        self.assertTrue(valid_orientation(orientation))

        orientation = 'A'
        self.assertFalse(valid_orientation(orientation))

    def test_validate_instruction(self):
        instruction = 'RFRFRFRF'
        self.assertTrue(valid_list_of_instructions(instruction))

        instruction = 'R F R F R FRF'
        self.assertTrue(valid_list_of_instructions(instruction))

        instruction = 'RFRFRFRD'
        self.assertFalse(valid_list_of_instructions(instruction))


#     def tearDown(self):
#         assert False

class TestMartianRobots(unittest.TestCase):
    def setUp(self):
        self.grid = [[0 for i in range(5)] for j in range(5)]

    def test_change_position(self):
        delta = get_position_change('N')
        self.assertEquals(delta['x'], 0)
        self.assertEquals(delta['y'], 1)

        delta = get_position_change('E')
        self.assertEquals(delta['x'], 1)
        self.assertEquals(delta['y'], 0)

        delta = get_position_change('S')
        self.assertEquals(delta['x'], 0)
        self.assertEquals(delta['y'], -1)

        delta = get_position_change('W')
        self.assertEquals(delta['x'], -1)
        self.assertEquals(delta['y'], 0)

    def test_over_the_edge(self):
        pos = {'x': 4, 'y': 4}
        self.assertFalse(over_the_edge(self.grid, pos))
        
        pos = {'x': 4, 'y': 5}
        self.assertTrue(over_the_edge(self.grid, pos))

    def test_build_output(self):
        pos = {'x': 4, 'y': 4, 'orientation': 'N', 'over_edge': False}
        expected = '4 4 N'
        self.assertEquals(build_output(pos), expected)

        pos = {'x': 4, 'y': 4, 'orientation': 'N', 'over_edge': True}
        expected = '4 4 N LOST'
        self.assertEquals(build_output(pos), expected)


#     def test_leave_scent(self):
#         assert False

#     def test_detect_scent_and_continue(self):
#         assert False

#     def test_ignore_other_robots(self):
#         assert False

#     def tearDown(self):
#         assert False

if __name__ == '__main__':
    unittest.main()
