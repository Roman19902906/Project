from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "LOGIN FORM IS NOT CORRECT"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LINK), "REGISTER FORM IS NOT CORRECT"

