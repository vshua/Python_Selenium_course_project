from selenium.webdriver.common import alert
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()

    def right_item_was_added_to_cart_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not present"
        assert self.is_element_present(*ProductPageLocators.ITEM_ADDED_MESSAGE
        ), "No alert that a product has been added to cart"
        product_name_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_message_text = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_MESSAGE).text
        print(product_name_text, added_message_text)
        assert product_name_text in added_message_text, \
            f"The alert contains wrong product name: {added_message_text} - {product_name_text}"
        assert True

    def cart_price_is_right(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not present"
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "No alert with cart status"
        message_text = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        print(message_text, product_cost)
        assert product_cost == message_text, \
            f"Product cost in cart is not equal to the product cost {message_text} != {product_cost}"
        assert True