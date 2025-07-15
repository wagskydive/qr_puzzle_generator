"""Trivia question generation module with LLM integration."""
from __future__ import annotations

import os
from typing import Dict, Optional

try:
    import openai  # type: ignore
except ImportError:  # pragma: no cover - openai optional
    openai = None  # type: ignore

import json
import requests


class TriviaGenerator:
    """Generate trivia questions using different providers."""

    def __init__(self, provider: Optional[str] = None):
        self.provider = (provider or os.getenv("TRIVIA_PROVIDER", "dummy")).lower()
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")

    def generate_question(self, clue: str) -> Dict[str, str]:
        """Return a trivia question and answer for a given clue."""
        if self.provider == "openai":
            return self._generate_openai(clue)
        if self.provider == "ollama":
            return self._generate_ollama(clue)
        return self._generate_dummy(clue)

    def _generate_openai(self, clue: str) -> Dict[str, str]:
        if openai is None:
            raise RuntimeError("openai package not installed")
        if not self.openai_key:
            raise RuntimeError("OPENAI_API_KEY not set")
        openai.api_key = self.openai_key
        prompt = f"Create one trivia question about {clue}. Return JSON with 'question' and 'answer'."
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        text = res.choices[0].message.content
        try:
            data = json.loads(text)
            return {"question": data.get("question", ""), "answer": data.get("answer", "")}
        except json.JSONDecodeError:
            # Fallback if response not JSON
            return {"question": text.strip(), "answer": ""}

    def _generate_ollama(self, clue: str) -> Dict[str, str]:
        payload = {
            "model": "llama3",
            "prompt": f"Create one trivia question about {clue}. Return JSON with 'question' and 'answer'.",
            "stream": False,
        }
        res = requests.post(self.ollama_url, json=payload, timeout=10)
        res.raise_for_status()
        text = res.json().get("response", "{}").strip()
        try:
            data = json.loads(text)
            return {"question": data.get("question", ""), "answer": data.get("answer", "")}
        except json.JSONDecodeError:
            return {"question": text, "answer": ""}

    def _generate_dummy(self, clue: str) -> Dict[str, str]:
        return {"question": f"Dummy question about {clue}?", "answer": "42"}

    def generate_from_rule(self, rule: str) -> Dict[str, str]:
        """Convenience wrapper to generate trivia from a puzzle rule."""
        return self.generate_question(rule)
