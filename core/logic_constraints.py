"""Logic Constraints puzzle type (Picross-style)."""
from __future__ import annotations

from typing import Dict, List


class LogicConstraints:
    """Represents a puzzle defined by row and column hints."""

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.row_hints = [self._compute_hints(row) for row in grid]
        self.col_hints = [
            self._compute_hints([grid[r][c] for r in range(len(grid))])
            for c in range(len(grid[0]))
        ] if grid else []

    @staticmethod
    def _compute_hints(line: List[int]) -> List[int]:
        hints: List[int] = []
        count = 0
        for cell in line:
            if cell:
                count += 1
            else:
                if count > 0:
                    hints.append(count)
                    count = 0
        if count > 0:
            hints.append(count)
        if not hints:
            hints.append(0)
        return hints

    def expected_hints(self) -> Dict[str, List[List[int]]]:
        """Return row and column hints."""
        return {"rows": self.row_hints, "cols": self.col_hints}

    def check_solution(self, player_grid: List[List[int]]) -> bool:
        """Validate a player's solution against expected hints."""
        if not player_grid or not self.grid:
            return False
        if len(player_grid) != len(self.grid) or len(player_grid[0]) != len(self.grid[0]):
            return False
        row_hints = [self._compute_hints(row) for row in player_grid]
        col_hints = [
            self._compute_hints([player_grid[r][c] for r in range(len(player_grid))])
            for c in range(len(player_grid[0]))
        ]
        return row_hints == self.row_hints and col_hints == self.col_hints
