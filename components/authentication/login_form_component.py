from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.input_email = page.get_by_test_id('login-form-email-input').locator('//div//input')
        self.input_password = page.get_by_test_id('login-form-password-input').locator('//div//input')

    def fill(self, email: str, password: str):
        self.input_email.fill(email)
        expect(self.input_email).to_have_value(email)
        self.input_password.fill(password)
        expect(self.input_password).to_have_value(password)

    def check_visible(self):
        expect(self.input_email).to_be_visible()
        expect(self.input_password).to_be_visible()