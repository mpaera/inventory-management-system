from app import app


def test_external_api():
    client = app.test_client()

    response = client.get("/external-api")

    assert response.status_code == 200