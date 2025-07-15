# Project Planning

This document tracks high-level milestones and the status of each task derived from `design.md.md`.

## Milestone 1 – MVP Foundation
- [x] Create project structure and setup script
- [ ] Implement **Binary Rows** game mode
- [ ] Implement **Binary Math** game mode
- [ ] Implement **Grid Navigation** game mode
- [ ] Build minimal Flask Web UI
- [ ] Design basic UI templates for each mode
- [ ] Implement game engine to route to selected mode
- [ ] Add save/load system for puzzles and player progress
- [ ] Add simple puzzle validation (client-side and server-side)

## Milestone 2 – Trivia Expansion
- [ ] Integrate OpenAI or Ollama API (configurable)
- [ ] Create `trivia_generator.py` to handle clue → prompt → question
- [ ] Generate trivia from puzzle rules (e.g. “Reveal row 3”)
- [ ] Store correct answers and map to puzzle actions
- [ ] UI form for trivia questions and answer handling
- [ ] Add scoring or unlock mechanic based on trivia

## Milestone 3 – Intermediate Game Modes
- [ ] Add **Logic Constraints** puzzle type
- [ ] Add **Modular Math Rules** puzzle type
- [ ] Improve grid rendering with helper visuals (row hints, highlights)
- [ ] Add visual feedback for incorrect moves or conflicting logic

## Milestone 4 – Advanced Logic & Replayability
- [ ] Add **Chess Pattern Challenges**
- [ ] Add **Direction-Based Clue Trails**
- [ ] Implement **Pattern Recognition/Masking** mechanic
- [ ] Build meta-puzzle layer that combines two or more mini-games
- [ ] Add “Insane” difficulty tier with layered instructions

## Milestone 5 – Polish & Deployment
- [ ] Add mobile/tablet-responsive web design (CSS/JS)
- [ ] Export puzzles to printable format (PDF)
- [ ] Add player progress tracking or login (optional)
- [ ] Package into installable app (Electron / PWA)
- [ ] Create a landing page and instructions for public testing
