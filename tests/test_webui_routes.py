from webui.app import app


def test_basic_routes():
    app.config["TESTING"] = True
    client = app.test_client()
    assert client.get("/").status_code == 200
    assert client.get("/game/binary_rows").status_code == 200
    assert client.get("/trivia").status_code == 200
