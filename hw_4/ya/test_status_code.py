import requests


# Тестовая функция
def test_status_code(url, expected_status_code):
    response = requests.get(url, timeout=5)
    assert response.status_code == expected_status_code, f"Expected {expected_status_code}, got {response.status_code}"


