import pytest

from .Pages.product_page import ProductPage
import time


@pytest.mark.parametrize('promo_offer', ["0"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.right_item_was_added_to_cart_message()
    # time.sleep(1000)
    page.cart_price_is_right()
