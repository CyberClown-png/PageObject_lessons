from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import MainPageLocators

import time


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_page_url()

    def should_be_product_page_url(self):
        current_url = self.browser.current_url
        assert current_url.find("?promo=newYear") != -1, "invalid product page url"

    def can_add_to_basket(self):
        try:
            css_selector = str(ProductPageLocators.ADD_TO_BASKET[1])
            button = self.browser.find_element_by_css_selector(css_selector)
            button.click()
        except NoSuchElementException:
            return False
        return True

    def price_in_basket_should_be_equal_price_the_book(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_BASKET), "basket price not found"
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "book price not found"
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert book_price == price_in_basket, "price in basket not equal price of book"

    def book_name_should_be_equal_name_book_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "basket book name not found"
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME_IN_BASKET), "book name not found"
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET).text
        assert book_name == book_name_in_basket, "name book not equal name book in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"



