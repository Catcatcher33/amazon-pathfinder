from random import randint
from tabnanny import check

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
    bfs = BreadthFirstPaths(grid)
    bfs.bfs(start_cell)
    path = bfs.path_to(end_cell, start_cell)
    return path


def set_obstacles(grid: Grid, obstacles: list) -> Grid:
    for obstacle in obstacles:
        grid.add_obstacle(*obstacle)


def check_possibilities(obstacles: list, removed: list, start_cell: tuple, end_cell: tuple):
    best_path: list = [0 for _ in range(99)]
    best_removed: tuple = (0,0)
    existing_path: bool = False
    for _ in range(len(obstacles)):
        removed_cell = obstacles.pop(randint(0, len(obstacles)-1))
        grid: Grid = setup()
        set_obstacles(grid, obstacles)
        path: list = compute_shortest_path(grid, start_cell, end_cell)
        if path is not None and len(best_path) > len(path): #  If this is the shortest path, go forward
            best_path: list = path
            best_removed: tuple = removed_cell
            existing_path = True
        else:
            continue
    if existing_path == True:
        return best_path, best_removed
    else:
        return check_possibilities()


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
    print('==== Bonus ====')
    grid: Grid = setup()
    obstacles: list = [(8,8), (8,9), (9,8)]
    set_obstacles(grid, obstacles)
    path: list = compute_shortest_path(grid, start_cell, end_cell)
    if path is not None:
        print(f'Path: {path}\nNumber of steps: {len(path)-1}\n')
    else:
        check_possibilities(obstacles, start_cell, end_cell)


if __name__ == '__main__':
    phase_1()
    phase_2()
    bonus()
