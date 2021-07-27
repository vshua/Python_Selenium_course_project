from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_any_items_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            f"There is an item is a cart, but should not be any"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE), \
            f"There should be a message for empty cart, but there is none"