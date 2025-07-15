"""Minimal Flask app for QR Puzzle Generator."""
from flask import Flask, render_template, jsonify
from puzzle_generator import PuzzleGenerator

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

if __name__ == '__main__':
    app.run(debug=True)
