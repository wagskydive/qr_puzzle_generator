
# QR Puzzle Generator – MVP Design Document

## 🎯 Objective

Build a modular puzzle game framework where different mini-games are used to progressively reveal a hidden QR code.  
The **MVP** will focus on the simplest game types for rapid development and testing.

## ✅ MVP Game Modes (Phase 1)

### 1. 🧮 Binary Rows
- One math question per **row**.
- Player inputs the binary answer by clicking grid squares:
  - **Black** = `1`
  - **White** = `0`
- System compares input to the expected binary pattern for that row.

### 2. 🔢 Binary Math
- One math question for the **whole puzzle**.
- The binary form of the answer is used to fill a row or section.
- Simplified version of Binary Rows.

### 3. 🧭 Grid Navigation
- Player receives directional instructions like:
  - “Start at (0,0), move 2 right, 1 down, mark square.”
- Correct navigation reveals black squares.
- Can include decoys or false paths.

## 🔄 Expansion (Phase 2)

### 4. ❓ Trivia Challenge (LLM-Driven)
- Trivia questions are generated via **LLM** (OpenAI or Ollama).
- Correct answers reveal puzzle clues or grid sections.
- Trivia topics can be themed (tech, science, history, etc.).

## 🗂 Project Structure

```plaintext
qr_puzzle_generator/
├── core/
│   ├── game_engine.py
│   ├── binary_rows.py
│   ├── binary_math.py
│   ├── grid_navigation.py
├── webui/
│   ├── app.py
│   └── templates/
│       ├── index.html
│       ├── game_binary_rows.html
│       ├── game_binary_math.html
│       ├── game_grid_nav.html
├── puzzles/
├── tests/
├── assets/
└── README.md
```

## 🛠 Development Tools

- Python 3.10+
- Flask
- Pillow / Matplotlib (optional for visual grid rendering)
- Optional: OpenAI / Ollama for trivia expansion

## 🧱 Setup Script (DEV_SETUP.sh)

```bash
#!/bin/bash
echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install flask pillow matplotlib

echo "Initializing Git repo..."
git init

echo "Folder structure:"
mkdir -p core webui/templates puzzles tests assets

echo "Done. You are ready to develop!"
```

## 📌 Development Phases

### ✅ Phase 1 – MVP (Binary & Navigation)
- [x] Create project structure and setup script
- [x] Implement **Binary Rows** game mode
- [x] Implement **Binary Math** game mode
- [x] Implement **Grid Navigation** game mode
- [x] Build minimal **Flask Web UI**
- [x] Design basic UI templates for each mode
- [x] Implement game engine to route to selected mode
- [ ] Add save/load system for puzzles and player progress
- [ ] Add simple puzzle validation (client-side and server-side)

### 🔜 Phase 2 – First Expansion: Trivia with LLM
- [ ] Integrate OpenAI or Ollama API (configurable)
- [ ] Create `trivia_generator.py` to handle clue → prompt → question
- [ ] Generate trivia from puzzle rules (e.g. “Reveal row 3”)
- [ ] Store correct answers and map to puzzle actions
- [ ] UI form for trivia questions and answer handling
- [ ] Add scoring or unlock mechanic based on trivia

### 🔜 Phase 3 – Intermediate Game Modes
- [ ] Add **Logic Constraints** (Picross-style) puzzle type
- [ ] Add **Modular Math Rules** (e.g. `(row + col) % 2 == 0`)
- [ ] Improve grid rendering with helper visuals (row hints, highlights)
- [ ] Add visual feedback for incorrect moves or conflicting logic

### 🔴 Phase 4 – Advanced Logic & Replayability
- [ ] Add **Chess Pattern Challenges**
- [ ] Add **Direction-Based Clue Trails**
- [ ] Implement **Pattern Recognition/Masking** mechanic
- [ ] Build meta-puzzle layer that combines two or more mini-games
- [ ] Add “Insane” difficulty tier with layered instructions

### 🎁 Phase 5 – Polish, Packaging & Deployment
- [ ] Add mobile/tablet-responsive web design (CSS/JS)
- [ ] Export puzzles to printable format (PDF)
- [ ] Add player progress tracking or login (optional)
- [ ] Package into installable app (Electron / PWA)
- [ ] Create a landing page + instructions for public testing
