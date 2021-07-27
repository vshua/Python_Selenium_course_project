from .base_page import BasePage
from .locators import BasePageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_be_cart_button(self):
        assert self.is_element_present(*BasePageLocators.BASKET_BTN), "Basket button is not presented"