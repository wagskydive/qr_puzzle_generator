#!/bin/bash
# Script to initialize development environment

echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install qrcode pillow matplotlib

echo "Creating project folder structure..."
mkdir -p assets/templates tests puzzles docs

echo "Initializing git repository..."
git init

echo "Done. You're ready to start developing!"

# Install Flask for Web UI
pip install flask
