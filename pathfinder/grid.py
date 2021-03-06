"""Contains information about all objects needed to store data about cells."""

class Cell:
    """Single cell in a 2D grid. Contains coordinates and a list of edges"""

    class Coordinates:
        """2D Cartesian coordinates."""

        def __init__(self, x: int, y: int):
            """Sole setter method for 2D Cartesian coordinates."""
            self.x: int = x
            self.y: int = y

    def __init__(self, x: int, y: int):
        """Initialises cell's coordinates and all edges connected to it."""
        self.coord = Cell.Coordinates(x, y)
        self.edges: list = []

    def edge(self, x, y):
        """
        Adds a pair of coordinates with a direct link to the current cell.

        No link is created in the current cases:
            - the cell already exists
            - the cell has invalid coordinates.
            - the cell has the same coordinates as the current cell.
        """
        if (x, y) in self.edges: #  Coordinates have already been registered.
            return
        if (x < 0 or x > 9) or (y < 0 or y > 9): #  Coordinates are outside of the grid's scope.
            return
        if x == self.coord.x and y == self.coord.y: #  Coordinates are that of the cell itself.
            return
        self.edges.append((x, y))

    def set_edges(self):
        """Create an edge between the current cell and all surrounding cells."""
        x = self.coord.x
        y = self.coord.y

        for i in range(0,3): # Add surrounding edges
            for j in range(0,3):
                self.edge(x-1+i, y-1+j)

    def remove_edge(self, x, y):
        """Given a set list of coordinates, removes the cell from the list of edges."""
        for i in self.edges:
            if i[0] == x and i[1] == y:
                self.edges.remove(i)


class Grid:
    """2D grid with the desired dimensions and all cell data."""

    def __init__(self, x_count, y_count):
        """Create all necessary cells."""
        self.cells: dict = {}
        for y in range(y_count):
            for x in range(x_count):
                cell = Cell(x, y)
                self.cells[(x, y)] = cell

    def connect_everything(self):
        """Connect each cell in the grid with the cells surrounding it."""
        for cell in self.cells.values():
            for i in range(0,3):
                for j in range(0,3):
                    cell.edge(cell.coord.x-1+i, cell.coord.y-1+j)

    def get_cell(self, x: int, y: int):
        """Given a list of coordinates, obtain a cell object from the grid."""
        return self.cells.get((x, y))

    def add_obstacle(self, x, y):
        """Given a set of coordinates, add an obstacle within the grid."""
        for i in range(0,3):
            for j in range(0,3):
                adjacent_cell = self.get_cell(x-1+i, y-1+j)
                if adjacent_cell is not None:
                    adjacent_cell.remove_edge(x, y)
        self.cells.pop((x, y))

    def set_obstacles(self, obstacles: list):
        """Set all obstacles."""
        for obstacle in obstacles:
            self.add_obstacle(*obstacle)


def generate_grid(obstacles: list, x_n: int=10, y_n: int = 10) -> Grid:
    """Creates a completed connected grid and adds obstacles."""
    grid = Grid(x_n, y_n)
    grid.connect_everything()
    grid.set_obstacles(obstacles)
    return grid
