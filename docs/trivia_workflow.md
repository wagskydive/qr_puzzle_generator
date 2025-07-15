# Trivia Workflow

Trivia questions are generated from puzzle rules using `TriviaGenerator`. Each rule describes which puzzle portion to reveal. For example, `"Reveal chunk 0"` becomes a trivia question whose correct answer unlocks that chunk in the game.

Questions can come from different providers (`dummy`, `openai`, or `ollama`). The returned dictionary contains both the question and its expected answer so the front end can validate the player's response.
