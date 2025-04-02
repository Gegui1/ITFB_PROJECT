import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://localhost:80")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FFService(), options=FFOptions())
    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(), options=EdgeOptions())
    elif browser_name == "yandex":
        driver = webdriver.Chrome(service=ChromeService())  # Yandex использует Chromium
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")


    driver.maximize_window()
    driver.url = url

    yield driver
    driver.quit()