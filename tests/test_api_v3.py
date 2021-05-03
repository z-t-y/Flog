from flask import current_app
from .helpers import register, login, get_api_v3_headers
from flog.models import User


def test_api_index(client):
    response = client.get("/api/v3/")
    data = response.get_json()
    assert data["api_version"] == "3.0"


def test_user(client):
    register(client)
    login(client, "test", "password")
    user_id = User.query.filter_by(username="test").first().id
    response = client.get(f"/api/v3/user/{user_id}/")
    data = response.get_json()
    assert data["username"] == "test"


def test_get_token(client):
    response = client.post(
        "/api/v3/token/",
        data=dict(
            username=current_app.config["FLOG_ADMIN"],
            password=current_app.config["FLOG_ADMIN_PASSWORD"],
        ),
    )
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data.get("access_token"), str)


def test_user(client):
    register(client)
    user = User.query.filter_by(username="test").first()
    response = client.get(f"/api/v3/user/{user.id}/")
    data = response.get_json()
    assert data["id"] == user.id

    user_data = {
        "name": "Real Name",
        "about_me": "A test user.",
        "location": "Nowhere",
        "password": "new_password"
    }
    response = client.put(f"/api/v3/user/{user.id}/", json=user_data, headers=get_api_v3_headers(client))
    assert response.status_code == 200
    assert user.name == user_data["name"]
    assert user.verify_password("new_password")

    response = client.patch(
        f"/api/v3/user/{user.id}/",
        json=user_data,
        headers=get_api_v3_headers(
            client,
            username=current_app.config["FLOG_ADMIN"],
            password=current_app.config["FLOG_ADMIN_PASSWORD"]
        )
    )
    assert response.status_code == 200
    assert user.locked
