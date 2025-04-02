from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import RegisterPage


def test_firstname_input_is_displayed(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(RegisterPage.FIRSTNAME_INPUT))
    assert browser.find_element(*RegisterPage.FIRSTNAME_INPUT).is_displayed(), "Кнопка не отображается"


def test_lastname_input_is_displayed(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(RegisterPage.LASTNAME_INPUT))
    assert browser.find_element(*RegisterPage.LASTNAME_INPUT).is_displayed(), "Кнопка не отображается"


def test_email_input_is_displayed(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(RegisterPage.EMAIL_INPUT))
    assert browser.find_element(*RegisterPage.EMAIL_INPUT).is_displayed(), "Кнопка не отображается"


def test_password_input_is_displayed(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(RegisterPage.PASSWORD_INPUT))
    assert browser.find_element(*RegisterPage.PASSWORD_INPUT).is_displayed(), "Кнопка не отображается"


def test_newsletter_checkbox_link_is_displayed(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(RegisterPage.NEWSLETTER_CHECKBOX))
    assert browser.find_element(*RegisterPage.NEWSLETTER_CHECKBOX).is_displayed(), "Кнопка не отображается"


def test_register_button_link_is_displayed(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(RegisterPage.REGISTER_BUTTON))
    assert browser.find_element(*RegisterPage.REGISTER_BUTTON).is_displayed(), "Кнопка не отображается"

