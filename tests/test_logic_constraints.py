from core.logic_constraints import LogicConstraints


def test_logic_constraints():
    grid = [
        [1, 0, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]
    puzzle = LogicConstraints(grid)
    hints = puzzle.expected_hints()
    assert hints["rows"] == [[1, 1], [2], [2]]
    assert hints["cols"] == [[2], [2], [1, 1]]
    assert puzzle.check_solution(grid)
    assert not puzzle.check_solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
