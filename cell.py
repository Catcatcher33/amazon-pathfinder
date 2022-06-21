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

if __name__ == '__main__':
    cell = Cell(1,1)
    cell.set_edges()
    print(cell.edges)
