from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn")

class BasketPageLocators():
    BASKET_ITEMS = (By.ID, "basket_formset")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner > p")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    ADD_SUCCESS_ITEM = (By.CSS_SELECTOR, ".alertinner")
    ADD_SUCCESS_ITEM_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_SUCCESS_CART = (By.CSS_SELECTOR, ".alertinner p")
    ADD_SUCCESS_CART_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
