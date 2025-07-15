# Puzzle Validation

The project validates puzzle solutions both on the client and the server. The web UI collects the player's grid clicks and submits them to `/api/validate_solution`. On the server side, `verifier.verify_puzzle` compares the submitted data to the stored puzzle representation.

This simple approach keeps the gameplay responsive while preventing players from bypassing puzzle rules.
