def test_register_success(client):
    response = client.post(
        "/auth/register",
        json={"login": "testuser", "email": "user@mail.com", "password": "pass123"},
    )
    assert response.status_code == 200


def test_register_duplicate_email_returns_409(client):
    payload = {"login": "testuser", "email": "dup@mail.com", "password": "pass123"}
    client.post("/auth/register", json=payload)

    response = client.post("/auth/register", json=payload)

    assert response.status_code == 409


def test_login_success(client):
    client.post(
        "/auth/register",
        json={"login": "authuser", "email": "auth@mail.com", "password": "pass123"},
    )

    response = client.post(
        "/auth/login",
        json={"email": "auth@mail.com", "password": "pass123"},
    )

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_unknown_email_returns_401(client):
    response = client.post(
        "/auth/login",
        json={"email": "noone@mail.com", "password": "bad"},
    )
    assert response.status_code == 401


def test_login_wrong_password_returns_401(client):
    client.post(
        "/auth/register",
        json={"login": "wronguser", "email": "wrongpass@mail.com", "password": "correct"},
    )

    response = client.post(
        "/auth/login",
        json={"email": "wrongpass@mail.com", "password": "wrong"},
    )

    assert response.status_code == 401
