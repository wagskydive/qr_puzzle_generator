import builtins
import types

import json

from trivia_generator import TriviaGenerator


def test_dummy_provider():
    tg = TriviaGenerator(provider="dummy")
    q = tg.generate_question("science")
    assert q["question"].startswith("Dummy question")
    assert q["answer"] == "42"


def test_openai_provider(monkeypatch):
    fake_response = types.SimpleNamespace(choices=[types.SimpleNamespace(message=types.SimpleNamespace(content=json.dumps({"question": "Q?", "answer": "A"})) )])

    class FakeCompletion:
        @staticmethod
        def create(model, messages, temperature):
            return fake_response

    fake_openai = types.SimpleNamespace(ChatCompletion=FakeCompletion)
    import trivia_generator as tg_mod
    monkeypatch.setattr(tg_mod, 'openai', fake_openai)

    tg = TriviaGenerator(provider="openai")
    tg.openai_key = "test"
    q = tg.generate_question("history")
    assert q == {"question": "Q?", "answer": "A"}


def test_generate_from_rule():
    tg = TriviaGenerator(provider="dummy")
    q = tg.generate_from_rule("Reveal row 3")
    assert "row 3" in q["question"]


