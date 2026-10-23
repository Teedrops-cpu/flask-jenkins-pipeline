from app import app

def test_home_returns_200():
    response = app.test_client().get("/")
    assert response.status_code == 200

def test_home_message():
    response = app.test_client().get("/")
    assert b"Hello from inside a Docker container!" in response.data
