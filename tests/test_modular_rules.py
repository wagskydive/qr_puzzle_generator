from core.modular_rules import ModularRules


def test_modular_rules():
    puzzle = ModularRules(size=3, mod=2, remainder=0)
    expected = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1],
    ]
    assert puzzle.expected_grid() == expected
    assert puzzle.check_solution(expected)
    assert not puzzle.check_solution([[0] * 3 for _ in range(3)])
