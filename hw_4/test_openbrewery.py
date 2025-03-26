import pytest
import requests
from jsonschema import validate


base_url = "https://api.openbrewerydb.org/"

def test_breweries_list():
    response = requests.get(f"{base_url}/v1/breweries?per_page=3")
    assert response.status_code == 200
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "address_1": {"type": "string"},
                "address_2": {"type": ["string", "null"]},
                "address_3": {"type": ["string", "null"]},
                "city": {"type": "string"},
                "state_province": {"type": "string"},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": ["string", "null"]},
                "latitude": {"type": ["string", "null"]},
                "phone": {"type": ["string", "null"]},
                "website_url": {"type": ["string", "null"]},
                "state": {"type": "string"},
                "street": {"type": "string"}
            },
            "required": ["id", "name", "brewery_type", "address_1", "city", "state_province", "postal_code", "country", "state", "street"]
        }
    }
    validate(instance=response.json(), schema=schema)


@pytest.mark.parametrize("page", [10, 55, None])
def test_breweries_page_limit(page):
    response = requests.get(f"{base_url}/v1/breweries?per_page={page}")
    assert response.status_code == 200
    data = response.json()

    if page is None:
        assert len(data) == 50
    else:
        assert len(data) == page


@pytest.mark.parametrize("num_requests", [5])
def test_random_breweries(num_requests):
    ids = set()
    for i in range(num_requests):
        response = requests.get(f"{base_url}/v1/breweries/random")
        assert response.status_code == 200
        data = response.json()
        assert 'id' in data[0]
        ids.add(data[0]['id'])
    assert len(ids) == num_requests


@pytest.mark.parametrize("size, expected_count", [(None, 1), (3, 3), (50, 50)])
def test_breweries_random_size(size, expected_count):
    response = requests.get(f"{base_url}/v1/breweries/random?size={size}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == expected_count


def test_breweries_meta():
    response = requests.get(f"{base_url}/v1/breweries/meta")
    assert response.status_code == 200
    data = response.json()
    assert "total" in data
    assert "page" in data
    assert "per_page" in data


