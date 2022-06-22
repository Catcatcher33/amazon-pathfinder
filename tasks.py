from random import randint
from itertools import combinations

from grid import generate_grid
from path import compute_shortest_path


def alternate_paths(obstacles: list, removed_count: int, start_cell: tuple, end_cell: tuple):
    '''
    In the event that a path cannot be computed, remove a given number of obstacles to find the next possible shortest path.
    '''
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


def execute(obstacles: list):
    '''
    With a given list of obstacles, find the shortest possible path.
    '''
    start_cell = (0,0)
    end_cell = (9,9)      
    path: list = compute_shortest_path(generate_grid(obstacles), start_cell, end_cell)
    print(f'Obstacles: {obstacles}')
    if path is not None:
        print(f'Path: {path}\nNumber of steps: {len(path)-1}\n')
    else:
        print(f'Unable to reach delivery point.')
        best_path, best_removed = alternate_paths(obstacles, 1, start_cell, end_cell)
        print(f'Best next possible path: {best_path}')
        print(f'The following obstacles need to be removed: {best_removed}')


def phase_1():
    '''
    Finds the shortest path for a grid with a predefined set of obstacles.
    '''
    print('==== Phase 1 ====')
    obstacles: list = [(7,7), (7,8), (8, 7), (9,7)]
    execute(obstacles)


def phase_2():
    ''' 
    Finds the shortest path for a grid with Phase 1's obstacles and an additional random 20 obstacles.
    '''
    print('==== Phase 2 ====')

    #  Create 20 individual obstacle coordinates
    obstacles: list = [(7,7), (7,8), (8, 7), (9,7)]
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
    '''
    For a set of obstacles where a path cannot be found, suggests the smallest possible 
    reduced set of obstacles for a path to be computed.
    '''
    print('==== Bonus ====')
    obstacles: list = [(8,9), (9,8), (8,8), (7,7), (7,8), (8,7), (7,9), (9,7)]
    execute(obstacles)