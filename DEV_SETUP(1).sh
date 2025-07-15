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
