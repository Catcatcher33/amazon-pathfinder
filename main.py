from cell import Cell

# implementing breadth first search blah blah

# Create the adjacency matrix. Shows if there's a link between two things.
# use an adjacency list.

'''
for adjacency:
each node is reachable from up, down, diagonal (4 ways), left, right. So 8 ways.
'''

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
                    print(f'FOR CELL {adjacent_cell.coord.x}, {adjacent_cell.coord.y}: -------')
                    print(f'BEFORE: {adjacent_cell.edges}')
                    adjacent_cell.remove_edge(x, y)
                    print(f'AFTER: {adjacent_cell.edges}')
        self.cells.pop((x, y))

if __name__ == '__main__':
    grid = Grid(10, 10)
    grid.connect_everything()
    grid.add_obstacle(9,7)
    print(grid.cells.keys())
    # print the path in the format [(x0, y0), (x1, y1), etc...]