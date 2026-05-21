from app.core.security.security import create_access_token


def auth_headers():
    token = create_access_token({"sub": "1"})
    return {"Authorization": f"Bearer {token}"}


def test_create_user(client):
    response = client.post("/users", json={"name": "Alice", "lastName": "Smith"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice"
    assert data["lastName"] == "Smith"
    assert "id" in data


def test_create_user_short_name_returns_422(client):
    response = client.post("/users", json={"name": "Al", "lastName": "Smith"})
    assert response.status_code == 422


def test_list_users_without_auth_returns_401(client):
    response = client.get("/users")
    assert response.status_code == 401


def test_list_users_with_auth(client):
    client.post("/users", json={"name": "Bob", "lastName": "Jones"})

    response = client.get("/users", headers=auth_headers())

    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "total" in data
    assert data["total"] >= 1


def test_get_user_by_id(client):
    create_res = client.post("/users", json={"name": "Carol", "lastName": "White"})
    user_id = create_res.json()["id"]

    response = client.get(f"/users/{user_id}", headers=auth_headers())

    assert response.status_code == 200
    assert response.json()["name"] == "Carol"


def test_get_user_not_found_returns_404(client):
    response = client.get("/users/9999", headers=auth_headers())
    assert response.status_code == 404


def test_update_user(client):
    create_res = client.post("/users", json={"name": "Dave", "lastName": "Brown"})
    user_id = create_res.json()["id"]

    response = client.put(
        f"/users/{user_id}",
        json={"name": "David", "lastName": "Brown"},
        headers=auth_headers(),
    )

    assert response.status_code == 200
    assert response.json()["name"] == "David"


def test_delete_user(client):
    create_res = client.post("/users", json={"name": "Eve", "lastName": "Green"})
    user_id = create_res.json()["id"]

    response = client.delete(f"/users/{user_id}", headers=auth_headers())

    assert response.status_code == 200
