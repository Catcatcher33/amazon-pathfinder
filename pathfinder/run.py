"""Main point of execution."""


from pathfinder.grid import generate_grid, Grid
from pathfinder.path import compute_shortest_path, alternate_paths
from pathfinder.terminal import TerminalUI


def execute(obstacles: list):
    """With a given list of obstacles, find the shortest possible path."""
    start_cell = (0,0)
    end_cell = (9,9)
    grid: Grid = generate_grid(obstacles)
    path: list = compute_shortest_path(grid, start_cell, end_cell)

    ui = TerminalUI(grid, start_cell, end_cell, x = 10, y = 10)
    ui.show_initialisation(obstacles)

    if path:
        ui.found_path(path)
    else:
        best_path, best_removed = alternate_paths(obstacles, 1, start_cell, end_cell)
        ui.no_path(best_path, best_removed)


def run(actions: list):
    """Runs every given action."""
    for action in actions:
        title, obstacles = action()
        print(f"Execute {title.lower()}? (y/n)")
        if input() != 'y':
            continue
        TerminalUI.title(title)
        execute(obstacles)
