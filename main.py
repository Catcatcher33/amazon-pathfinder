from typing_extensions import Self
from numpy import true_divide


# implementing breadth first search blah blah

# Create the adjacency matrix. Shows if there's a link between two things.
# use an adjacency list.

'''
for adjacency:
each node is reachable from up, down, diagonal (4 ways), left, right. So 8 ways.
'''

class Node:

    class Coordinates:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

    def __init__(self, x, y): # edges is a set of nodes.
        self.coordinates = Node.Coordinates(x, y)
        self.edges = set()
    
    def add_edge(self, node: Self):
        self.edges.add(node)
        return self

    def remove_edge(self, node: Self):
        self.edges.remove(node)
        return self
        

class Grid:

    def __init__(self):
        pass


class Graph:

    def __init__(self, node_count: int=100):
        self.adj = [[] for _ in range(node_count)]

        pass



class BreadthFirstSearch:

    def __init__(self):

        
        self.marked = [-1 for ]
        self.edge_to = []
        self.distance_to_source = []

    def bfs(self):
        pass

# print the path in the format [(x0, y0), (x1, y1), etc...]