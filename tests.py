""" Unit tests for Martian Robots program"""
import unittest

from martian_robots import valid_grid_size

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

#     def test_validate_starting_position(self):
#         assert False

#     def test_validate_starting_orientation(self):
#         assert False

#     def test_validate_instruction_length(self):
#         assert False

#     def test_validate_instruction(self):
#         assert False

#     def tearDown(self):
#         assert False

# class TestMartianRobots(unittest.TestCase):
#     def setUp(self):
#         assert False

#     def test_change_position(self):
#         assert False

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
