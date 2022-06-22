from random import randint

from grid import Grid
from path import BreadthFirstPaths


def setup() -> Grid:
    grid = Grid(10, 10)
    grid.connect_everything()
    return grid


def default_args(func):
    def wrapper():
        start_cell: tuple = (0, 0)
        end_cell: tuple = (9, 9)
        func(start_cell, end_cell)
    return wrapper


def compute_shortest_path(grid: Grid, start_cell: int, end_cell: int) -> list:
    #  Explore the graph.
    bfs = BreadthFirstPaths(grid)
    bfs.bfs(start_cell)

    # Find the shortest path.
    path = bfs.path_to(end_cell, start_cell)
    return path


def set_obstacles(grid: Grid, obstacles: list) -> Grid:
    for obstacle in obstacles:
        grid.add_obstacle(*obstacle)



@default_args
def phase_1(start_cell: int, end_cell: int):
    print('==== Phase 1 ====')
    grid: Grid = setup()
    obstacles: list = [(7,7), (7,8), (8, 7), (9,7)]
    set_obstacles(grid, obstacles)
    path: list = compute_shortest_path(grid, start_cell, end_cell)
    print(f'Path: {path}\nNumber of steps: {len(path)-1}\n')


@default_args
def phase_2(start_cell: int, end_cell: int):
    print('==== Phase 2 ====')
    grid = setup()

    #  Create 20 individual obstacle coordinates
    obstacles: list = []
    i: int = 0
    while i < 20:
        x: int = randint(0, 9)
        y: int = randint(0, 9) 
        if (x, y) in obstacles or (x, y) == start_cell or (x, y) == end_cell:
            continue
        else:
            obstacles.append((x, y))
            i+=1

    set_obstacles(grid, obstacles)
    path: list = compute_shortest_path(grid, start_cell, end_cell)
    print(f'Path: {path}\n')

@default_args
def bonus(start_cell: int, end_cell: int):
    pass


if __name__ == '__main__':
    phase_1()
    phase_2()
    bonus()
