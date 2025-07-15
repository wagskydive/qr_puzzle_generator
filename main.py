"""CLI entry point for creating sample puzzles."""
from puzzle_generator import PuzzleGenerator
from core.game_engine import GameEngine


def create_sample_puzzles():
    engine = GameEngine()
    gen = PuzzleGenerator()

    br = engine.create('binary_rows', questions=[('1+1', 2), ('3+1', 4)])
    gen.save(br, 'puzzle.json')
    print('Saved Binary Rows puzzle to puzzle.json')


if __name__ == '__main__':
    create_sample_puzzles()
