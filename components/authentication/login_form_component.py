from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.input import Input
from elements.text import Text


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'authentication-ui-course-title-text', 'Title')
        self.input_email = Input(page,'login-form-email-input','Email')
        self.input_password = Input(page,'login-form-password-input', 'Password')

    def fill(self, email: str, password: str):
        self.input_email.fill(email)
        self.input_email.check_have_value(email)
        self.input_password.fill(password)
        self.input_password.check_have_value(password)

    def check_visible(self):
        self.title.check_visible()
        self.input_email.check_visible()
        self.input_password.check_visible()