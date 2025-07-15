import json
import os
from webui.app import app, TRIVIA_SCORE


def test_trivia_endpoints(tmp_path):
    puzzle_path = tmp_path / "puzzle.json"
    puzzle_data = {
        "mode": "grid_navigation",
        "grid": [[1, 0], [0, 1]],
        "trivia": {"question": "Q?", "answer": "A", "action": "reveal"}
    }
    puzzle_path.write_text(json.dumps(puzzle_data))

    old_cwd = os.getcwd()
    os.chdir(tmp_path)
    app.config["TESTING"] = True
    client = app.test_client()

    res = client.get("/api/trivia_question")
    assert res.status_code == 200
    assert res.get_json()["question"] == "Q?"

    res = client.post("/api/trivia_answer", json={"answer": "A"})
    data = res.get_json()
    assert data["status"] == "correct"
    first_score = data["score"]

    res = client.post("/api/trivia_answer", json={"answer": "wrong"})
    data = res.get_json()
    assert data["status"] == "incorrect"
    assert data["score"] == first_score

    os.chdir(old_cwd)
