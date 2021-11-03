from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL doesn't contain the word 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not present"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password1_input = self.browser.find_element(*LoginPageLocators.PASSWORD1_INPUT)
        password1_input.send_keys(password)
        password2_input = self.browser.find_element(*LoginPageLocators.PASSWORD2_INPUT)
        password2_input.send_keys(password)
        submit_btn = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_btn.click()
