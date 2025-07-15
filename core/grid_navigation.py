"""Grid Navigation puzzle logic."""
from typing import List, Tuple

Move = Tuple[str, int]

class GridNavigation:
    """Represents a grid navigation puzzle."""
    DIRECTIONS = {
        'U': (0, -1),
        'D': (0, 1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    def __init__(self, size: int, start: Tuple[int, int] = (0, 0)):
        self.size = size
        self.start = start
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def apply_instructions(self, moves: List[Move]) -> List[List[int]]:
        """Return grid after applying navigation moves."""
        x, y = self.start
        self.grid[y][x] = 1
        for direction, steps in moves:
            if direction not in self.DIRECTIONS:
                raise ValueError(f"Invalid direction: {direction}")
            dx, dy = self.DIRECTIONS[direction]
            for _ in range(steps):
                x += dx
                y += dy
                if not (0 <= x < self.size and 0 <= y < self.size):
                    raise ValueError("Move out of bounds")
                self.grid[y][x] = 1
        return self.grid
