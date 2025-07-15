"""Binary Math puzzle logic."""
from typing import Tuple

class BinaryMath:
    """Represents a binary math puzzle."""
    def __init__(self, question: str, answer: int):
        self.question = question
        self.answer = answer
        self.binary = bin(answer)[2:]

    def expected_pattern(self) -> str:
        """Return the binary representation used in the puzzle."""
        return self.binary

    def check_answer(self, player_binary: str) -> bool:
        """Validate the player's binary answer."""
        return self.binary == player_binary.lstrip('0') or self.binary == player_binary.zfill(len(self.binary))
