from typing_extensions import Self

class Node:
    
    class Coordinates:
        def __init__(self, x: int, y: int):
            self._x = x
            self._y = y
        
        def get(self):
            return (self._x, self._y)
        
    def __init__(self, x: int, y: int, is_obstacle: bool = False):
        self._coord: Node.Coordinates = Node.Coordinates(x, y)
        self._edges: set = set()
        self._obstacle: bool = is_obstacle
    
    def add_edge(self, node: Self):
        self.edges.add(node)
        return self
    
    def remove_edge(self, node: Self):
        self.edges.remove(node)
        return self
    
    def is_obstacle(self):
        self._obstacle: bool = True
    
    def is_accessible(self):
        self._obstacle: bool = False