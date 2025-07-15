# QR Puzzle Workflow

1. **Generate QR Matrix** – `qr_processor.generate_matrix` converts any text into a matrix of `1` and `0` values.
2. **Segment Matrix** – `qr_puzzle_generator.segment_matrix` splits the matrix into smaller chunks.
3. **Map to Puzzles** – `qr_puzzle_generator.matrix_to_puzzles` converts each chunk into a mini-game puzzle. Currently chunks become `grid_navigation` puzzles.
4. **(Optional) Attach Trivia** – `qr_puzzle_generator.generate_qr_puzzles_with_trivia` can attach a trivia question to each chunk, storing the expected answer along with a reference to the chunk to reveal.
5. **Render in Web UI** – the puzzles are presented in the browser where players solve them to gradually reveal the full QR code.
