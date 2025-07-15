# QR Puzzle Generator - MVP

This project demonstrates a minimal puzzle framework with three game modes:
Binary Rows, Binary Math and Grid Navigation. A small Flask app renders the
puzzles in the browser.

The Web UI includes a basic validation feature. Clicking **Check Solution**
sends the current grid state to the server, which verifies it against the saved
puzzle data.

## Running

```bash
# Generate a sample puzzle
python3 main.py
# Launch the web UI
python3 webui/app.py
```
