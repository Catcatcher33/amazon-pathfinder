"""Contains all custom grids. All functions should return a set list of obstacles and the configuration title."""


from random import randint


def phase_1():
    """Finds the shortest path for a grid with a predefined set of obstacles."""
    return "Phase 1", [(7,7), (7,8), (8, 7), (9,7)]


def phase_2() -> list:
    """
    Finds the shortest path for a grid with Phase 1's
    obstacles and an additional random 20 obstacles.
    """
    #  Create 20 individual obstacle coordinates
    obstacles: list = [(7,7), (7,8), (8, 7), (9,7)]
    i: int = 0
    while i < 20:
        x: int = randint(0, 9)
        y: int = randint(0, 9)
        if (x, y) in obstacles or (x, y) == (0,0) or (x, y) == (9,9):
            continue
        obstacles.append((x, y))
        i+=1
    return "Phase 2", obstacles


def bonus() -> list:
    """
    For a set of obstacles where a path cannot be found, suggests the smallest possible
    reduced set of obstacles for a path to be computed.
    """
    return "Bonus", [(8,9), (9,8), (8,8), (7,7), (7,8), (8,7), (7,9), (9,7)]
