"""Modular Math Rules puzzle type."""
from __future__ import annotations

from typing import List


class ModularRules:
    """Puzzle where black squares satisfy a modular rule."""

    def __init__(self, size: int, mod: int, remainder: int = 0):
        self.size = size
        self.mod = mod
        self.remainder = remainder
        self.grid = [
            [1 if (r + c) % mod == remainder else 0 for c in range(size)]
            for r in range(size)
        ]

    def expected_grid(self) -> List[List[int]]:
        """Return the generated grid."""
        return self.grid

    def check_solution(self, player_grid: List[List[int]]) -> bool:
        """Validate that ``player_grid`` matches the generated pattern."""
        return player_grid == self.grid
