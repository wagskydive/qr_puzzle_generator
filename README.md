# QR Puzzle Generator - MVP

This project demonstrates a minimal puzzle framework with three game modes:
Binary Rows, Binary Math and Grid Navigation. A small Flask app renders the
puzzles in the browser.

The Web UI includes a basic validation feature. Clicking **Check Solution**
sends the current grid state to the server, which verifies it against the saved
puzzle data.  
Milestone 2 introduces a trivia generator used to reveal parts of a puzzle.

## Running

```bash
# Generate a sample puzzle
python3 main.py
# Launch the web UI
python3 webui/app.py
```

## Trivia Generation

`TriviaGenerator` can create questions using OpenAI or Ollama depending on the
`TRIVIA_PROVIDER` environment variable. When neither provider is configured it
falls back to a dummy implementation which is used in tests.
