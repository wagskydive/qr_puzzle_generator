from core.grid_navigation import GridNavigation


def test_grid_nav():
    puzzle = GridNavigation(3)
    grid = puzzle.apply_instructions([('R', 1), ('D', 1)])
    assert grid == [
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
