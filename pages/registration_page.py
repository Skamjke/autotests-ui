from pages.base_page import BasePage
from playwright.sync_api import Page,expect

class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.reg_email_input = page.get_by_test_id('registration-form-email-input').locator('//div//input')
        self.reg_username_input = page.get_by_test_id('registration-form-username-input').locator('//div//input')
        self.reg_password_input = page.get_by_test_id('registration-form-password-input').locator('//div//input')
        self.reg_button = page.get_by_test_id('registration-page-registration-button')

    def fill_registration_form(self, email: str, username: str, password: str):
        self.reg_email_input.fill(email)
        expect(self.reg_email_input).to_have_value(email)
        self.reg_username_input.fill(username)
        expect(self.reg_username_input).to_have_value(username)
        self.reg_password_input.fill(password)
        expect(self.reg_password_input).to_have_value(password)

    def click_reg_button(self):
        self.reg_button.click()

