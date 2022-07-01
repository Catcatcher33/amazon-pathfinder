"""Contains all data structured needed for exploring cells and edges between them."""

from itertools import combinations

from pathfinder.grid import Grid, generate_grid


class BreadthFirstPaths:
    """Breadth-First Search implementation used to explore the grid."""

    def __init__(self, grid: Grid):
        """Intialises the grid and all structures needed to store important data."""
        self.grid = grid
        self.visited: dict = dict.fromkeys(grid.cells.keys(), False)
        self.distance_to_source: dict = dict.fromkeys(grid.cells.keys(), -1)
        self.edge_to: dict = dict.fromkeys(grid.cells.keys(), -1)
        self.queue: list = []

    def bfs(self, start_cell: tuple):
        """Search the graph to register cells and edges."""
        self.queue.append(start_cell)
        self.visited[start_cell] = True
        self.distance_to_source[start_cell] = 0

        while self.queue:
            start_cell = self.queue.pop(0)
            for adj in self.grid.get_cell(*start_cell).edges:

                if self.visited[adj] is False:
                    self.queue.append(adj)
                    self.distance_to_source[adj] = self.distance_to_source[start_cell] + 1
                    self.visited[adj] = True
                    self.edge_to[adj] = start_cell

    def has_path_to(self, cell):
        """Check if there exists a path from one cell to another."""
        return self.distance_to_source[cell] != -1

    def path_to(self, cell, start_cell):
        """Collect the path from a given start cell to a given target cell."""
        if not self.has_path_to(cell):
            return None
        path = []
        current_cell = cell
        while current_cell != start_cell:
            path.append(current_cell)
            current_cell = self.edge_to[current_cell]
        path.append(start_cell)
        path.reverse()
        return path


def alternate_paths(obstacles: list, removed_count: int, start_cell: tuple, end_cell: tuple):
    """
    In the event that a path cannot be computed, remove a given number
    of obstacles to find the next possible shortest path.
    """
    best_path: list = [0 for _ in range(99)]
    best_removed_obstacles: list = []
    path_exists: bool = False

    for removed_obstacles in combinations(obstacles, removed_count):
        obstacle_list = obstacles.copy()
        for obstacle in obstacle_list:
            if obstacle in removed_obstacles:
                obstacle_list.remove(obstacle)

        path: list = compute_shortest_path(generate_grid(obstacle_list), start_cell, end_cell)

        if path is not None and len(path) < len(best_path):
            best_path = path
            best_removed_obstacles = removed_obstacles
            path_exists = True

    if path_exists:
        return best_path, list(best_removed_obstacles)
    return alternate_paths(obstacles, removed_count+1, start_cell, end_cell)


def compute_shortest_path(grid: Grid, start_cell: int, end_cell: int) -> list:
    """Return the shortest possible itinerary between a given start cell and a given target cell."""
    bfs = BreadthFirstPaths(grid)
    bfs.bfs(start_cell)
    path = bfs.path_to(end_cell, start_cell)
    return path
