from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, f"The 'login' is not in '{url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_in = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_in.send_keys(email)
        password_in = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_in.send_keys(password)
        confirm_password_in = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        confirm_password_in.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        success_message = self.browser.find_element(*LoginPageLocators.SUCCES_MESSAGE)