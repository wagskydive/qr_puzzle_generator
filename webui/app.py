"""Minimal Flask app for QR Puzzle Generator."""
from flask import Flask, render_template, jsonify, request
from puzzle_generator import PuzzleGenerator
from verifier import verify_puzzle

# simple in-memory score for trivia questions
TRIVIA_SCORE = 0

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


@app.route('/trivia')
def trivia_page():
    """Render the trivia question page."""
    return render_template('trivia.html')

@app.route('/api/load_solution')
def load_solution():
    try:
        data = PuzzleGenerator().load('puzzle.json')
        return jsonify({'status': 'success', **data})
    except FileNotFoundError:
        return jsonify({'status': 'error', 'message': 'no puzzle'}), 404


@app.route('/api/trivia_question')
def trivia_question():
    """Return the stored trivia question if available."""
    try:
        puzzle = PuzzleGenerator().load('puzzle.json')
    except FileNotFoundError:
        return jsonify({'status': 'error', 'message': 'no puzzle'}), 404
    trivia = puzzle.get('trivia')
    if isinstance(trivia, list):
        trivia = trivia[0] if trivia else None
    if not trivia:
        return jsonify({'status': 'error', 'message': 'no trivia'}), 404
    return jsonify({'status': 'success', 'question': trivia.get('question', '')})


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


@app.route('/api/trivia_answer', methods=['POST'])
def trivia_answer():
    """Validate a trivia answer and update score."""
    global TRIVIA_SCORE
    try:
        puzzle = PuzzleGenerator().load('puzzle.json')
    except FileNotFoundError:
        return jsonify({'status': 'error', 'message': 'no puzzle'}), 404
    trivia = puzzle.get('trivia', {})
    expected = str(trivia.get('answer', '')).strip().lower()
    data = request.get_json(silent=True) or {}
    answer = str(data.get('answer', '')).strip().lower()
    if answer == expected and expected:
        TRIVIA_SCORE += 1
        return jsonify({'status': 'correct', 'score': TRIVIA_SCORE})
    return jsonify({'status': 'incorrect', 'score': TRIVIA_SCORE})

if __name__ == '__main__':
    app.run(debug=True)
