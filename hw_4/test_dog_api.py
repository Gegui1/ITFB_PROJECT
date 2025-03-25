import pytest
import requests


base_url = "https://dog.ceo/api"

def test_get_breeds():
    response = requests.get(f"{base_url}/breeds/list/all")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert isinstance(data["message"], dict)


def test_random_image():
    response = requests.get(f"{base_url}/breeds/image/random")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert isinstance(data["message"], str)
    assert data["message"].endswith((".jpg", ".jpeg", ".png"))
    image_response = requests.get(data["message"])
    assert image_response.status_code == 200
    assert "image" in image_response.headers["Content-Type"]


def test_random_image_variety():
    images = set()
    for i in range(10):
        response = requests.get(f"{base_url}/breeds/image/random")
        data = response.json()
        images.add(data["message"])
    assert len(images) == 10, "Not all images are unique"


@pytest.mark.parametrize("count", [1, 49, 50])
def test_multiple_random_images_count(count):
    response = requests.get(f"{base_url}/breeds/image/random/{count}")
    data = response.json()
    assert len(data["message"]) == count, f"Expected {count} images, but got {len(data['message'])}"


@pytest.mark.parametrize("breed", ["hound", "bulldog", "terrier"])
def test_breed_images(breed):
    response = requests.get(f"{base_url}/breed/{breed}/images")
    data = response.json()
    assert isinstance(data["message"], list), f"Expected a list, but got {type(data['message'])}"
    assert len(data["message"]) > 0, "Expected images, but got an empty list"