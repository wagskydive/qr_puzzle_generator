"""Game engine to switch between puzzle modes."""
from typing import Any, Dict

from .binary_rows import BinaryRows
from .binary_math import BinaryMath
from .grid_navigation import GridNavigation
from .logic_constraints import LogicConstraints
from .modular_rules import ModularRules

class GameEngine:
    """Factory-like interface to create puzzle instances."""
    def create(self, mode: str, **kwargs) -> Any:
        mode = mode.lower()
        if mode == "binary_rows":
            return BinaryRows(kwargs.get("questions", []))
        if mode == "binary_math":
            return BinaryMath(kwargs.get("question", ""), kwargs.get("answer", 0))
        if mode == "grid_navigation":
            return GridNavigation(kwargs.get("size", 5), kwargs.get("start", (0, 0)))
        if mode == "logic_constraints":
            return LogicConstraints(kwargs.get("grid", []))
        if mode == "modular_rules":
            return ModularRules(
                kwargs.get("size", 5),
                kwargs.get("mod", 2),
                kwargs.get("remainder", 0),
            )
        raise ValueError(f"Unknown game mode: {mode}")
