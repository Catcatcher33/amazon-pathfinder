class Cell:

    class Coordinates:

        def __init__(self, x: int, y: int):
            self.x: int = x
            self.y: int = y

    def __init__(self, x: int, y: int, obstacle: bool=False):
        # Must make sure it doesn't get created if the coordinates are invalid.
        # I should list the dimensions or something
        self.coord = Cell.Coordinates(x, y)
        self.edges: list = [] # list of coordinates.
        self.obstacle: bool = True

    def edge(self, x, y):
        '''
        Adds a pair of coordinates with a direct link to the current cell.
        
        No link is created in the current cases:
            - the cell already exists
            - the cell has invalid coordinates.
            - the cell has the same coordinates as the current cell.
        '''
        if (x, y) in self.edges:
            return
        if (x < 0 or x > 9) or (y < 0 or y > 9):
            return
        if x == self.coord.x and y == self.coord.y: #  coordinates are its own.
            return
        self.edges.append((x, y))
    
    def set_edges(self):
        x = self.coord.x
        y = self.coord.y

        # add surrounding edges
        for i in range(0,3):
            for j in range(0,3):
                self.edge(x-1+i, y-1+j)

    def remove_edge(self, x, y):
        for i in self.edges:
            if i[0] == x and i[1] == y:
                #print(i)
                self.edges.remove(i)


class Grid:
    def __init__(self, x_count, y_count):
        self.cells: dict = {}

        # Generate the entire grid.
        for y in range(y_count):
            for x in range(x_count):
                cell = Cell(x, y)
                self.cells[(x, y)] = cell
    
    def connect_everything(self):
        for cell in self.cells.values():
            for i in range(0,3):
                for j in range(0,3):
                    cell.edge(cell.coord.x-1+i, cell.coord.y-1+j)

    def get_cell(self, x: int, y: int):
        return self.cells.get((x, y))

    def add_obstacle(self, x, y):
        for i in range(0,3):
            for j in range(0,3):
                adjacent_cell = self.get_cell(x-1+i, y-1+j)
                if adjacent_cell is not None:
                    #print(f'FOR CELL {adjacent_cell.coord.x}, {adjacent_cell.coord.y}: -------')
                    #print(f'BEFORE: {adjacent_cell.edges}')
                    adjacent_cell.remove_edge(x, y)
                    #print(f'AFTER: {adjacent_cell.edges}')
        self.cells.pop((x, y))

    def set_obstacles(self, obstacles: list):
        for obstacle in obstacles:
            self.add_obstacle(*obstacle)

def setup(x_n: int=10, y_n: int = 10) -> Grid:
    grid = Grid(x_n, x_n)
    grid.connect_everything()
    return grid
