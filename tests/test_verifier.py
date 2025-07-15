from verifier import verify_grid, verify_puzzle


def test_verify_grid():
    expected = [[1, 0], [0, 1]]
    assert verify_grid(expected, [[1, 0], [0, 1]])
    assert not verify_grid(expected, [[1, 1], [0, 1]])


def test_verify_puzzle():
    grid_puzzle = {"mode": "grid_navigation", "grid": [[1, 0], [0, 1]]}
    assert verify_puzzle(grid_puzzle, {"grid": [[1, 0], [0, 1]]})
    assert not verify_puzzle(grid_puzzle, {"grid": [[1, 1], [0, 1]]})

    row_puzzle = {"mode": "binary_rows", "rows": ["10", "01"]}
    assert verify_puzzle(row_puzzle, {"rows": ["10", "01"]})
    assert not verify_puzzle(row_puzzle, {"rows": ["10", "10"]})

    math_puzzle = {"mode": "binary_math", "pattern": "1010"}
    assert verify_puzzle(math_puzzle, {"binary": "1010"})
    assert not verify_puzzle(math_puzzle, {"binary": "1111"})
