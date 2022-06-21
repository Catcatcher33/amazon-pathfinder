from grid import Grid

# implementing breadth first search blah blah

# Create the adjacency matrix. Shows if there's a link between two things.
# use an adjacency list.

class BreadthFirstPaths:

    def __init__(self, grid):
        self.visited: dict = dict.fromkeys(grid.cells.keys(), False)
        self.distance_to_source: dict = dict.fromkeys(grid.cells.keys(), -1)
        self.edge_to: dict = dict.fromkeys(grid.cells.keys(), -1)
        self.queue: list = []

    def bfs(self, start_cell: tuple):
        self.queue.append(start_cell)
        self.visited[start_cell] = True
        self.distance_to_source[start_cell] = 0

        while self.queue:
            start_cell = self.queue.pop(0)
            print(f'FOR CELL {start_cell}: EDGES ARE: {grid.get_cell(*start_cell).edges}')

            for adj in grid.get_cell(*start_cell).edges:
                
                if self.visited[adj] == False: #and distance_to_source[adj] != -1:
                    self.queue.append(adj)
                    self.distance_to_source[adj] = self.distance_to_source[start_cell] + 1
                    self.visited[adj] = True
                    self.edge_to[adj] = start_cell

    def has_path_to(self, cell):
        return self.distance_to_source[cell] != -1

    def path_to(self, cell, start_cell):
        if not self.has_path_to(cell):
            return None
        path = []
        x = cell
        while x != start_cell:
            path.append(x)
            x = self.edge_to[x]
        path.append(start_cell)
        return path


if __name__ == '__main__':
    grid = Grid(10, 10)
    grid.connect_everything()
    #grid.add_obstacle(9,7)
    #grid.add_obstacle(8,7)
    #grid.add_obstacle(6,7)
    #grid.add_obstacle(6,8)
    grid.add_obstacle(7,7)
    grid.add_obstacle(7,8)
    grid.add_obstacle(8,7)
    grid.add_obstacle(9,7)
    #print(grid.cells.keys())
    bfs = BreadthFirstPaths(grid)
    bfs.bfs((0,0))
    path = bfs.path_to((9,9), (0,0))
    print(path)
    
    # print the path in the format [(x0, y0), (x1, y1), etc...]