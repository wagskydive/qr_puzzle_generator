"""Puzzle verification utilities."""
from typing import Any, Dict, List


def verify_grid(expected: List[List[int]], attempt: List[List[int]]) -> bool:
    """Return True if two grids are identical."""
    if len(expected) != len(attempt):
        return False
    for row_exp, row_att in zip(expected, attempt):
        if row_exp != row_att:
            return False
    return True


def verify_puzzle(puzzle: Dict[str, Any], attempt: Dict[str, Any]) -> bool:
    """Validate a puzzle attempt based on puzzle metadata."""
    mode = puzzle.get("mode")
    if mode == "grid_navigation":
        return verify_grid(puzzle.get("grid", []), attempt.get("grid", []))
    if mode == "binary_rows":
        return puzzle.get("rows") == attempt.get("rows")
    if mode == "binary_math":
        return puzzle.get("pattern") == attempt.get("binary")
    return False
