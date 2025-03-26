import pytest
import requests
from jsonschema import validate


base_url = "https://jsonplaceholder.typicode.com"


@pytest.mark.parametrize("id", [1, 5, 10])
def test_get_resource(id):
    response = requests.get(f"{base_url}/posts/{id}")
    assert response.status_code == 200
    assert response.json()["id"] == id


@pytest.mark.parametrize("title, body, userId", [
    ("test", "message", 2),
    ("hello", "world", 3)
])
def test_create_post(title, body, userId):
    data = {"title": title, "body": body, "userId": userId}
    response = requests.post(f"{base_url}/posts", json=data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["title"] == title
    assert response_data["body"] == body
    assert response_data["userId"] == userId
    assert "id" in response_data


def test_update_resource():
    data = {"id": 1, "title": "foo", "body": "bar", "userId": 1}
    response = requests.put(f"{base_url}/posts/1", json=data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == data["id"]
    assert response_data["title"] == data["title"]
    assert response_data["body"] == data["body"]
    assert response_data["userId"] == data["userId"]


def test_delete_resource():
    response = requests.delete(f"{base_url}/posts/1")
    assert response.status_code == 200
    assert len(response.json()) == 0


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_comments_for_post(post_id):
    response = requests.get(f"{base_url}/posts/{post_id}/comments")
    assert response.status_code == 200
    data = response.json()
    for comment in data:
        assert comment["postId"] == post_id
