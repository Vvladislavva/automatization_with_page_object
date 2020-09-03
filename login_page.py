from .base_page import BasePage
from .locators import LoginPageLocators
import faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Incorrect URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        f = faker.Faker()
        registration_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registration_email.send_keys(f.email())
        password = f.name()
        registration_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        registration_password.send_keys(password)
        submit_password = self.browser.find_element(*LoginPageLocators.SUBMIT_PASSWORD)
        submit_password.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()
