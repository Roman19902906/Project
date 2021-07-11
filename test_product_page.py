import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.base_page import BasePage
import time
from pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.test_guest_can_see_product_to_basket()
    time.sleep(1)


@pytest.mark.parametrize('promo_offer',
                         ("?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4",
                          "?promo=offer5", "?promo=offer6",
                          pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                          "?promo=offer8", "?promo=offer9"))
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.test_guest_can_add_product_to_basket()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    page.test_guest_can_see_product_to_basket()
    time.sleep(1)
    page.test_guest_can_see_price_to_basket()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_add_product_to_basket()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()
    time.sleep(1)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()
    time.sleep(1)


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_add_product_to_basket()
    page.test_message_disappeared_after_adding_product_to_basket()
    time.sleep(1)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.page = BasePage(browser, link)
        self.page.open()
        self.page.register_new_user(email, password, browser)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.test_guest_cant_see_success_message()

    # def test_user_can_add_product_to_basket(self, browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    # page = ProductPage(browser, link)
    # page.open()
    # page.test_guest_can_add_product_to_basket()
    # page.test_guest_can_see_product_to_basket()
    # time.sleep(2)
    # page.test_guest_can_see_price_to_basket()
