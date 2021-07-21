from selenium.webdriver.common import alert
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()

    def right_item_was_added_to_cart_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name.get_attribute('text')
        added_message = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_MESSAGE)
        message_text = added_message.get_attribute('text')
        assert str(product_name_text) in str(message_text), "Product name is not presented in the alert"
        assert True

    def cart_price_is_right(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price = product_price.get_attribute('text')
        cart_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        cart = cart_price.get_attribute('text')
        assert str(price) == str(cart), "Basket total differs from product price"
        assert True


