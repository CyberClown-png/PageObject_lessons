from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import MainPageLocators


class BasketPage(BasePage):

    def can_open_basket(self):
        try:
            xpath_selector = str(MainPageLocators.BASKET_BUTTON[1])
            button = self.browser.find_element_by_xpath(xpath_selector)
            button.click()
        except NoSuchElementException:
            return False
        return True

    def should_be_empty_basket(self):
        assert self.is_element_present(*MainPageLocators.BASKET_EMPTY), "basket don't empty, or not found"
