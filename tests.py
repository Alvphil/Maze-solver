import unittest
from maze import Maze

class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_columns = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows,num_columns,10,10)
        self.assertEqual(
            len(m1._cells), 
            num_rows
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_columns,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_entrance(self):
        num_columns = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows,num_columns,10,10)
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False
        )

    def test_maze_exit(self):
        num_columns = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows,num_columns,10,10)
        self.assertEqual(
            m1._cells[num_rows-1][num_columns-1].has_right_wall,
            False
        )

    def test_reset_visited(self):
        num_columns = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows,num_columns,0,0)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )

if __name__ == "__main__":
    unittest.main()
