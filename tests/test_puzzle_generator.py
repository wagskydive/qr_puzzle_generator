import os
from puzzle_generator import PuzzleGenerator
from core.binary_rows import BinaryRows


def test_save_and_load(tmp_path):
    puzzle = BinaryRows([('1+1', 2)])
    path = tmp_path / 'p.json'
    gen = PuzzleGenerator()
    gen.save(puzzle, path)
    data = gen.load(path)
    assert data['mode'] == 'binary_rows'
    assert data['rows'] == ['10']
