

class BreadthFirstPaths:

    def __init__(self, grid):
        self.grid = grid
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
            for adj in self.grid.get_cell(*start_cell).edges:
                
                if self.visited[adj] == False: #and distance_to_source[adj] != -1:
                    self.queue.append(adj)
                    self.distance_to_source[adj] = self.distance_to_source[start_cell] + 1
                    self.visited[adj] = True
                    self.edge_to[adj] = start_cell

    def has_path_to(self, cell):
        return self.distance_to_source[cell] != -1

    def path_to(self, cell, start_cell):
        if not self.has_path_to(cell):
            return 'Unable to reach delivery point.'
        path = []
        x = cell
        while x != start_cell:
            path.append(x)
            x = self.edge_to[x]
        path.append(start_cell)
        path.reverse()
        return path