from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    FORM_LINK = (By.CSS_SELECTOR, "div.page_inner")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages div.alertinner strong")
    PRODUCT_IN_PAGE = (By.CSS_SELECTOR, "#content_inner h1:first-child")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRICE_IN_PAGE = (By.CSS_SELECTOR, "#content_inner p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE = (By.CSS_SELECTOR, ".basket-mini a")
    PRODUCT_IN_BASKET_PAGE = (By.CSS_SELECTOR, "#content_inner h2")
    EMPTY_BASKET_PAGE = (By.CSS_SELECTOR, "#messages")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")