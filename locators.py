from selenium.webdriver.common.by import By


class Links():
    BASKET = "/basket/"


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.XPATH, "//*[contains(@href, 'basket')]")
    BASKET_EMPTY = (By.XPATH, "//*[@id='content_inner']/p")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators() :
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages :nth-child(3) > .alertinner > p strong")
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages :nth-child(1) > .alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1).alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
