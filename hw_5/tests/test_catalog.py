from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import CatalogPage


def test_compare_button_is_displayed(browser):
    browser.get(browser.url + "/catalog/smartphone")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(CatalogPage.COMPARE_BUTTON))
    assert browser.find_element(*CatalogPage.COMPARE_BUTTON).is_displayed(), "Кнопка не отображается"


def test_list_view_is_displayed(browser):
    browser.get(browser.url + "/catalog/smartphone")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(CatalogPage.LIST_VIEW_BUTTON))
    assert browser.find_element(*CatalogPage.LIST_VIEW_BUTTON).is_displayed(), "Кнопка не отображается"


def test_sort_dropdown_is_displayed(browser):
    browser.get(browser.url + "/catalog/smartphone")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(CatalogPage.SORT_DROPDOWN))
    assert browser.find_element(*CatalogPage.SORT_DROPDOWN).is_displayed(), "Кнопка не отображается"


def test_limit_dropdown_is_displayed(browser):
    browser.get(browser.url + "/catalog/smartphone")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(CatalogPage.LIMIT_DROPDOWN))
    assert browser.find_element(*CatalogPage.LIMIT_DROPDOWN).is_displayed(), "Кнопка не отображается"


def test_grid_button_is_displayed(browser):
    browser.get(browser.url + "/catalog/smartphone")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(CatalogPage.GRID_BUTTON))
    assert browser.find_element(*CatalogPage.GRID_BUTTON).is_displayed(), "Кнопка не отображается"

