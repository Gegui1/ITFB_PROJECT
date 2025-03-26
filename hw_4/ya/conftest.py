import pytest


def pytest_addoption(parser):
    print(">>> pytest_addoption executed!")
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="URL to test"
    )
    parser.addoption(
        "--status_code",
        type=int,
        default=200,
        help="Expected status code"
    )

@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def expected_status_code(request):
    return request.config.getoption("--status_code")