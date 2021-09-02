import time
import pytest

from .basket_page import BasketPage
from .locators import ProductPageLocators
from .product_page import ProductPage

"""
@pytest.mark.parametrize('link', [1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.can_add_to_basket()
    page.solve_quiz_and_get_code()
    page.price_in_basket_should_be_equal_price_the_book()
    page.book_name_should_be_equal_name_book_in_basket()
"""


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.can_add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "find success message element after adding product in basket (not ok)"


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "find success message element (not ok)"


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.can_add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "after adding in basket element doesn't hide (not ok)"


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = BasketPage(browser, link)
    page.open()
    page.can_open_basket()
    page.should_be_empty_basket()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = BasketPage(browser, link)
    page.open()
    page.can_open_basket()
    page.should_be_empty_basket()

@pytest.fixture(scope = "function")
class TestUserAddToBasketFromProductPage:
    def test_user_cant_see_product_in_basket_opened_from_main_page(browser):
        link = "http://selenium1py.pythonanywhere.com/ru/"
        page = BasketPage(browser, link)
        page.open()
        page.can_open_basket()
        page.should_be_empty_basket()

    def test_user_cant_see_product_in_basket_opened_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = BasketPage(browser, link)
        page.open()
        page.can_open_basket()
        page.should_be_empty_basket()