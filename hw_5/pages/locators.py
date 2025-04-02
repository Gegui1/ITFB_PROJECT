from selenium.webdriver.common.by import By

class Homepage:
    WISHLIST_BUTTON = (By.XPATH, '//*[@id="wishlist-total"]/span')
    CART_BUTTON = (By.XPATH, '//*[@id="header-cart"]/div/button')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="search"]/button')
    SEARCH_INPUT = (By.XPATH, '//*[@id="search"]/input')
    CAROUSEL_BUTTONS = (By.XPATH, '//*[@id="carousel-banner-0"]/button/span')


class CatalogPage:
    COMPARE_BUTTON = (By.XPATH, '//*[@id="compare-total"]/span')
    LIST_VIEW_BUTTON = (By.XPATH, '//*[@id="button-list"]')
    SORT_DROPDOWN = (By.XPATH, '//*[@id="input-sort"]')
    LIMIT_DROPDOWN = (By.XPATH, '//*[@id="input-limit"]')
    GRID_BUTTON = (By.XPATH, '//*[@id="button-grid"]')


class ProductPage:
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="button-cart"]')
    REVIEWS_BUTTON = (By.XPATH, '//*[@id="content"]/ul/li[2]/a')
    QUANTITY_INPUT = (By.XPATH, '//*[@id="input-quantity"]')
    ADD_TO_WISHLIST_BUTTON = (By.XPATH, '//*[@id="content"]//button[1]')
    COMPARE_PRODUCT_BUTTON = (By.XPATH, '//*[@id="content"]//button[2]')


class LoginPage:
    USERNAME_INPUT = (By.XPATH, "//*[@id='input-username']")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='input-password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    OPENCART_HEADER_LINK = (By.XPATH, '//*[@id="header"]/div/a')


class RegisterPage:
    FIRSTNAME_INPUT = (By.XPATH, "//*[@id='input-firstname']")
    LASTNAME_INPUT = (By.XPATH, "//*[@id='input-lastname']")
    EMAIL_INPUT = (By.XPATH, "//*[@id='input-email']")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='input-password']")
    NEWSLETTER_CHECKBOX = (By.XPATH, "//*[@id='input-newsletter']")
    REGISTER_BUTTON = (By.XPATH, "//*[@id='form-register']/div/button")