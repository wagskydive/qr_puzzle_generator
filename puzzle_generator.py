"""High level puzzle generator."""
import json
from typing import List, Tuple

from core.binary_rows import BinaryRows
from core.binary_math import BinaryMath
from core.grid_navigation import GridNavigation


class PuzzleGenerator:
    """Create and persist puzzles."""

    def save(self, puzzle, path: str) -> None:
        """Save puzzle representation to JSON."""
        data = {}
        if isinstance(puzzle, BinaryRows):
            data = {"mode": "binary_rows", "rows": puzzle.expected_rows()}
        elif isinstance(puzzle, BinaryMath):
            data = {"mode": "binary_math", "pattern": puzzle.expected_pattern()}
        elif isinstance(puzzle, GridNavigation):
            data = {"mode": "grid_navigation", "grid": puzzle.grid}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def load(self, path: str):
        """Load puzzle representation from JSON."""
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
