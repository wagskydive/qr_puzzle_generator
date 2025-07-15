"""Binary Rows game logic."""
from typing import List, Tuple

class BinaryRows:
    """Represents a binary rows puzzle."""
    def __init__(self, questions: List[Tuple[str, int]]):
        """Create puzzle from a list of (question, answer) tuples."""
        self.questions = questions
        self.rows = [bin(ans)[2:] for _, ans in questions]
        self.width = max(len(r) for r in self.rows) if self.rows else 0
        # left pad rows to uniform width
        self.rows = [r.zfill(self.width) for r in self.rows]

    def expected_rows(self) -> List[str]:
        """Return list of expected binary rows."""
        return self.rows

    def check_row(self, index: int, player_row: str) -> bool:
        """Validate a player's binary string for the given row index."""
        if index < 0 or index >= len(self.rows):
            raise IndexError("Row index out of range")
        return self.rows[index] == player_row.zfill(self.width)
