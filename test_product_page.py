import time

import pytest

from .product_page import ProductPage

@pytest.mark.parametrize('link', [1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  7, 8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.can_add_to_basket()
    page.solve_quiz_and_get_code()
    page.price_in_basket_should_be_equal_price_the_book()
    page.book_name_should_be_equal_name_book_in_basket()



