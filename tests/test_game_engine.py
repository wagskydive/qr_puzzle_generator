from core.game_engine import GameEngine


def test_create_binary_rows():
    engine = GameEngine()
    puzzle = engine.create('binary_rows', questions=[('1+1', 2)])
    assert puzzle.expected_rows() == ['10']
