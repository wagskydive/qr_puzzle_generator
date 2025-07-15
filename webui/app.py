"""Minimal Flask app for QR Puzzle Generator."""
from flask import Flask, render_template, jsonify, request
from puzzle_generator import PuzzleGenerator
from verifier import verify_puzzle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/<mode>')
def game(mode):
    template = {
        'binary_rows': 'game_binary_rows.html',
        'binary_math': 'game_binary_math.html',
        'grid_nav': 'game_grid_nav.html'
    }.get(mode, 'index.html')
    return render_template(template)

@app.route('/api/load_solution')
def load_solution():
    try:
        data = PuzzleGenerator().load('puzzle.json')
        return jsonify({'status': 'success', **data})
    except FileNotFoundError:
        return jsonify({'status': 'error', 'message': 'no puzzle'}), 404


@app.route('/api/validate_solution', methods=['POST'])
def validate_solution():
    """Validate a posted puzzle solution."""
    try:
        puzzle = PuzzleGenerator().load('puzzle.json')
    except FileNotFoundError:
        return jsonify({'status': 'error', 'message': 'no puzzle'}), 404
    attempt = request.get_json(silent=True) or {}
    success = verify_puzzle(puzzle, attempt)
    return jsonify({'status': 'success' if success else 'failure'})

if __name__ == '__main__':
    app.run(debug=True)
