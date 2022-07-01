"""All functions used to show parts of the terminal interface for the program."""


class TerminalUI:
    """User Interface for the Terminal, showing all results of the program to the user."""

    def __init__(self, grid, start_cell: tuple, end_cell: tuple, **dimensions):
        """Registers the grid's visual data."""
        self.grid = grid
        self.start_cell = start_cell
        self.end_cell = end_cell
        self.max_x = dimensions['x']
        self.max_y = dimensions['y']

    def title(title: str):
        """Shows the title to the user."""
        print(f'====== {title} ======')

    def _separator(self):
        """Draws a breaking line separator"""
        print(f"{''.join(['-' for _ in range(22)])}")

    def _cell_type(self, x: int, y: int, path=None):
        """ Draws the cell based on its type."""
        if (x, y) == self.start_cell:
            return '🧍' # start cell
        if (x, y) == self.end_cell:
            return '⛳️' # target cell
        if path and (x, y) in path:
            return '🟩'
        if (x, y) in self.grid.cells.keys():
            return '⬜️' #  free cell
        return '❌' #  obstacle

    def _draw_grid(self, path=None):
        """Draws the grid, with or without a path."""
        print('  0 1 2 3 4 5 6 7 8 9 ')
        i: int = 0
        for y in range(self.max_y):
            print(f'{i} ', end='')
            for x in range(self.max_x):
                print(f'{self._cell_type(x, y, path)}', end='')
            print('')
            i+=1

    def _init_grid(self):
        """Draws the very first grid."""
        self._draw_grid()

    def _path(self, path: list):
        """Draws a grid with a path."""
        print("\nProposed path:")
        self._draw_grid(path)

    def no_path(self, best_path, best_removed):
        """Explains that no path is possible, and shows suggestions for a new possible path."""
        print('Unable to reach delivery point.')
        print(f'Best next possible path: {best_path}')
        print(f'The following obstacles need to be removed: {best_removed}')

    def show_initialisation(self, obstacles: list):
        """Shows the intialised grid."""
        self._init_grid()
        self._separator()
        print(f'Obstacles: {obstacles}')

    def found_path(self, path: list):
        """Shows the found possible path."""
        self._path(path)
        print(f'Path: {path}\nNumber of steps: {len(path)-1}\n')
