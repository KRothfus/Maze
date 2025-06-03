import unittest

from graphics import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
        
    def test_maze_create_cells100x1(self):
        num_cols = 1
        num_rows = 100
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
        
    def test_maze_create_cells100x100(self):
        num_cols = 100
        num_rows = 100
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    
    # def test_maze_create_cells12x0(self):
    #     num_cols = 12
    #     num_rows = 0
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(
    #         len(m1._Maze__cells),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m1._Maze__cells[0]),
    #         num_rows,
    #     )
    
    def test_break_entrance_and_exit_first(self):
        num_cols = 12
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__break_entrance_and_exit()
        self.assertFalse(m1._Maze__cells[0][0].has_top_wall)
        
    def test_break_entrance_and_exit_last(self):
        num_cols = 12
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__break_entrance_and_exit()
        self.assertFalse(m1._Maze__cells[num_cols-1][num_rows-1].has_bottom_wall)
if __name__ == "__main__":
    unittest.main()