from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import LoginPage


def test_username_input_is_displayed(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(LoginPage.USERNAME_INPUT))
    assert browser.find_element(*LoginPage.USERNAME_INPUT).is_displayed(), "Кнопка не отображается"


def test_password_input_is_displayed(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(LoginPage.PASSWORD_INPUT))
    assert browser.find_element(*LoginPage.PASSWORD_INPUT).is_displayed(), "Кнопка не отображается"


def test_submit_button_is_displayed(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(LoginPage.SUBMIT_BUTTON))
    assert browser.find_element(*LoginPage.SUBMIT_BUTTON).is_displayed(), "Кнопка не отображается"


def test_opencart_link_is_displayed(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(LoginPage.OPENCART_LINK))
    assert browser.find_element(*LoginPage.OPENCART_LINK).is_displayed(), "Кнопка не отображается"


def test_opencart_header_link_is_displayed(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(LoginPage.OPENCART_HEADER_LINK))
    assert browser.find_element(*LoginPage.OPENCART_HEADER_LINK).is_displayed(), "Кнопка не отображается"

