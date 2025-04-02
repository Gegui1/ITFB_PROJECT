from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Homepage


def test_wish_list_button_is_displayed(browser):
    browser.get(browser.url)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Homepage.WISHLIST_BUTTON))
    assert browser.find_element(*Homepage.WISHLIST_BUTTON).is_displayed(), "Кнопка не отображается"


def test_cart_button_is_displayed(browser):
    browser.get(browser.url)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Homepage.CART_BUTTON))
    assert browser.find_element(*Homepage.CART_BUTTON).is_displayed(), "Кнопка не отображается"

def test_search_button_is_displayed(browser):
    browser.get(browser.url)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Homepage.SEARCH_BUTTON))
    assert browser.find_element(*Homepage.SEARCH_BUTTON).is_displayed(), "Кнопка не отображается"


def test_search_input_is_displayed(browser):
    browser.get(browser.url)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Homepage.SEARCH_INPUT))
    assert browser.find_element(*Homepage.SEARCH_INPUT).is_displayed(), "Кнопка не отображается"


def test_carousel_buttons_is_displayed(browser):
    browser.get(browser.url)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Homepage.CAROUSEL_BUTTONS))
    assert browser.find_element(*Homepage.CAROUSEL_BUTTONS).is_displayed(), "Кнопка не отображается"

