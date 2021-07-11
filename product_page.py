from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
import time


class ProductPage(BasePage):
    def test_guest_can_add_product_to_basket(self):
        basket_page = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_page.click()

    def test_guest_can_see_product_to_basket(self):
        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET)
        product_in_page = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_PAGE)
        assert product_in_basket.text == product_in_page.text, "There is no match name with the product in the basket and on the page"

    def test_guest_can_see_price_to_basket(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        price_in_page = self.browser.find_element(*ProductPageLocators.PRICE_IN_PAGE)
        assert price_in_page.text == price_in_basket.text, "There is no match price with the product in the basket and on the page"

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
