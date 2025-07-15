"""Generate mini-game puzzles from a QR code matrix."""
from __future__ import annotations

from typing import Any, Dict, List

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


def matrix_to_puzzles(matrix: List[List[int]], chunk_size: int = 3) -> List[Dict[str, Any]]:
    """Map a QR matrix to grid navigation puzzles."""
    engine = GameEngine()
    puzzles: List[Dict[str, Any]] = []
    for chunk in segment_matrix(matrix, chunk_size):
        puzzle = engine.create("grid_navigation", size=len(chunk))
        puzzle.grid = chunk
        puzzles.append({"mode": "grid_navigation", "grid": chunk})
    return puzzles


def generate_qr_puzzles(data: str, chunk_size: int = 3) -> List[Dict[str, Any]]:
    """High-level helper to create puzzles from ``data``."""
    matrix = generate_matrix(data)
    return matrix_to_puzzles(matrix, chunk_size)

