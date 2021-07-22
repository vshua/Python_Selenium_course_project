from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-noicon.alert-info p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME =(By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    ITEM_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages .alert.alert-safe.alert-noicon.alert-success:nth-child(1) strong")