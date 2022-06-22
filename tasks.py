from random import randint

from grid import setup, Grid
from path import compute_shortest_path


def check_possibilities(obstacles: list, removed_count: int, start_cell: tuple, end_cell: tuple):
    # need to fix this, it looks awful lmfao
    best_path: list = [0 for _ in range(99)]
    best_removed: list = []
    existing_path: bool = False

    if removed_count > len(obstacles):
        raise RuntimeError("Bug: the number of required removed objects has overpassed the number of obstacles.")
    
    for _ in range(len(obstacles)):
        removed_cells: list = []
        extra_obstacles = obstacles.copy()
        for i in range(removed_count):
            removed_cells.append(extra_obstacles.pop(randint(0, len(extra_obstacles)-1)))

        grid: Grid = setup()
        grid.set_obstacles(extra_obstacles)

        path: list = compute_shortest_path(grid, start_cell, end_cell)

        if path is not None and len(best_path) > len(path): #  If this is the shortest path, go forward
            best_path = path
            best_removed = removed_cells
            existing_path = True
        else:
            continue
    if existing_path == True:
        return best_path, best_removed
    else:
        return check_possibilities(obstacles, removed_count+1, start_cell, end_cell)


def execute(obstacles: list):
    start_cell = (0,0)
    end_cell = (9,9)      
    grid: Grid = setup()
    grid.set_obstacles(obstacles)
    path: list = compute_shortest_path(grid, start_cell, end_cell)
    print(f'Obstacles: {obstacles}')
    if path is not None:
        print(f'Path: {path}\nNumber of steps: {len(path)-1}\n')
    else:
        print(f'Unable to reach delivery point.')
        best_path, best_removed = check_possibilities(obstacles, 1, start_cell, end_cell)
        print(f'Best next possible path: {best_path}')
        print(f'Need to remove the following obstacles at coordinates: {best_removed}')


def phase_1():
    print('==== Phase 1 ====')
    obstacles: list = [(7,7), (7,8), (8, 7), (9,7)]
    execute(obstacles)


def phase_2():
    print('==== Phase 2 ====')

    #  Create 20 individual obstacle coordinates
    obstacles: list = []
    i: int = 0
    while i < 20:
        x: int = randint(0, 9)
        y: int = randint(0, 9) 
        if (x, y) in obstacles or (x, y) == (0,0) or (x, y) == (9,9):
            continue
        else:
            obstacles.append((x, y))
            i+=1
    
    execute(obstacles)


def bonus():
    print('==== Bonus ====')
    obstacles: list = [(7,8), (8,7), (7,7), (7,9), (9,7), (6,6), (8,8), (8,9), (9,8)]
    execute(obstacles)