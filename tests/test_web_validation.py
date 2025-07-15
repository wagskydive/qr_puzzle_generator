import json
import os
from webui.app import app


def test_validate_solution_endpoint(tmp_path):
    puzzle_path = tmp_path / "puzzle.json"
    puzzle_data = {"mode": "grid_navigation", "grid": [[1, 0], [0, 1]]}
    puzzle_path.write_text(json.dumps(puzzle_data))

    old_cwd = os.getcwd()
    os.chdir(tmp_path)
    app.config["TESTING"] = True
    client = app.test_client()

    res = client.post("/api/validate_solution", json={"grid": [[1, 0], [0, 1]]})
    assert res.get_json()["status"] == "success"

    res = client.post("/api/validate_solution", json={"grid": [[1, 1], [0, 1]]})
    assert res.get_json()["status"] == "failure"
    os.chdir(old_cwd)
