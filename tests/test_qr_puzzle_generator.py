from qr_puzzle_generator import segment_matrix, matrix_to_puzzles, generate_qr_puzzles
from qr_processor import generate_matrix


def test_segment_matrix():
    matrix = [
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
    ]
    chunks = segment_matrix(matrix, 2)
    assert len(chunks) == 4
    assert chunks[0] == [[1, 0], [0, 1]]


def test_matrix_to_puzzles():
    matrix = [[1, 0], [0, 1]]
    puzzles = matrix_to_puzzles(matrix, chunk_size=2)
    assert puzzles == [{"mode": "grid_navigation", "grid": matrix}]


def test_generate_qr_puzzles():
    puzzles = generate_qr_puzzles("data", chunk_size=2)
    assert puzzles
    assert all(p["mode"] == "grid_navigation" for p in puzzles)
