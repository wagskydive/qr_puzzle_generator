"""Generate mini-game puzzles from a QR code matrix."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from core.game_engine import GameEngine
from qr_processor import generate_matrix


def segment_matrix(matrix: List[List[int]], size: int) -> List[List[List[int]]]:
    """Split a matrix into ``size`` x ``size`` chunks."""
    chunks: List[List[List[int]]] = []
    for y in range(0, len(matrix), size):
        for x in range(0, len(matrix[0]), size):
            chunk = [row[x : x + size] for row in matrix[y : y + size]]
            chunks.append(chunk)
    return chunks


def matrix_to_puzzles(
    matrix: List[List[int]],
    chunk_size: int = 3,
    trivia: Optional["TriviaGenerator"] = None,
) -> List[Dict[str, Any]]:
    """Map a QR matrix to grid navigation puzzles.

    If ``trivia`` is provided, each chunk includes a trivia question and answer
    to gate revealing that portion of the QR code.
    """
    engine = GameEngine()
    puzzles: List[Dict[str, Any]] = []
    for idx, chunk in enumerate(segment_matrix(matrix, chunk_size)):
        puzzle = engine.create("grid_navigation", size=len(chunk))
        puzzle.grid = chunk
        entry: Dict[str, Any] = {"mode": "grid_navigation", "grid": chunk}
        if trivia is not None:
            q = trivia.generate_from_rule(f"Reveal chunk {idx}")
            entry["trivia"] = {**q, "action": f"reveal_chunk_{idx}"}
        puzzles.append(entry)
    return puzzles


def generate_qr_puzzles(data: str, chunk_size: int = 3) -> List[Dict[str, Any]]:
    """High-level helper to create puzzles from ``data``."""
    matrix = generate_matrix(data)
    return matrix_to_puzzles(matrix, chunk_size)


def generate_qr_puzzles_with_trivia(
    data: str,
    chunk_size: int = 3,
    provider: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Create puzzles from ``data`` and attach trivia questions."""
    from trivia_generator import TriviaGenerator

    matrix = generate_matrix(data)
    tg = TriviaGenerator(provider=provider)
    return matrix_to_puzzles(matrix, chunk_size, trivia=tg)

