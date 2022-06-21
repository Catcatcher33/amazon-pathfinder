from typing_extensions import Self

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

    def add_edge(self, x, y):
        ''' Adds a pair of coordinates with a direct link to the current cell.'''
        # don't add if the edge is listed as an obstacle.
        self.edges.append((x, y))
    
    def set_edges(self):
        x = self.coord.x
        y = self.coord.y

        if 0 <= x < 9:
            self.add_edge(x+1, y) #  east

            if 0 <= y < 9 :
                self.add_edge(x, y+1) #  south
                self.add_edge(x+1, y+1) #  southeast
            
            if 0 < y <= 9:
                self.add_edge(x, y-1) #  north
                self.add_edge(x+1, y-1) # northeast

        if 0 < x <= 9:

            self.add_edge(x-1, y) #  west

            if 0 <= y < 9 :
                self.add_edge(x, y+1)  # south
                self.add_edge(x-1, y+1) #  southwest
            
            if 0 < y <= 9:
                self.add_edge(x, y-1) #  north
                self.add_edge(x-1, y-1) # northwest     


cell = Cell(1,1)
cell.set_edges()
print(cell.edges)
