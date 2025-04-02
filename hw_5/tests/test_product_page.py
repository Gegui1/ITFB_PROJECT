from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import ProductPage


def test_add_button_is_displayed(browser):
    browser.get(browser.url + "/product/smartphone/iphone")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ProductPage.ADD_TO_CART_BUTTON))
    assert browser.find_element(*ProductPage.ADD_TO_CART_BUTTON).is_displayed(), "Кнопка не отображается"


def test_reviews_button_is_displayed(browser):
    browser.get(browser.url + "/product/smartphone/iphone")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ProductPage.REVIEWS_BUTTON))
    assert browser.find_element(*ProductPage.REVIEWS_BUTTON).is_displayed(), "Кнопка не отображается"


def test_quantity_button_is_displayed(browser):
    browser.get(browser.url + "/product/smartphone/iphone")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ProductPage.QUANTITY_INPUT))
    assert browser.find_element(*ProductPage.QUANTITY_INPUT).is_displayed(), "Кнопка не отображается"


def test_add_wishlist_button_is_displayed(browser):
    browser.get(browser.url + "/product/smartphone/iphone")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ProductPage.ADD_TO_WISHLIST_BUTTON))
    assert browser.find_element(*ProductPage.ADD_TO_WISHLIST_BUTTON).is_displayed(), "Кнопка не отображается"


def test_compare_buttons_is_displayed(browser):
    browser.get(browser.url + "/product/smartphone/iphone")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ProductPage.COMPARE_PRODUCT_BUTTON))
    assert browser.find_element(*ProductPage.COMPARE_PRODUCT_BUTTON).is_displayed(), "Кнопка не отображается"

