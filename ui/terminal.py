from grid import Grid


class TerminalUI: # Another addition would be to change the color of the terminal output to make the rest more readable

    def __init__(self, grid: Grid, start_cell: tuple, end_cell: tuple, **dimensions):
        self.grid = grid
        self.start_cell = start_cell
        self.end_cell = end_cell
        self.max_x = dimensions['x']
        self.max_y = dimensions['y']

    def separator(self):
        print(f"{''.join(['-' for _ in range(22)])}")

    def cell_type(self, x: int, y: int, path=None): # could I add an aditional condition? to determine if this is for the path?
        if (x, y) == self.start_cell:
            return '🧍' # start cell
        elif (x, y) == self.end_cell:
            return '⛳️' # target cell
        elif path is not None and (x, y) in path:
            return '🟩'
        elif (x, y) in self.grid.cells.keys():
            return '⬜️' #  free cell
        return '❌' #  obstacle

    def draw_grid(self, path=None):
        print('  0 1 2 3 4 5 6 7 8 9 ')
        i: int = 0
        for y in range(self.max_y):
            print(f'{i} ', end='')
            for x in range(self.max_x):
                print(f'{self.cell_type(x, y, path)}', end='')
            print('')
            i+=1

    def init_grid(self):
        print("Grid:")
        self.draw_grid()

    def path(self, path: list):
        print("Proposed path:")
        self.draw_grid(path)
