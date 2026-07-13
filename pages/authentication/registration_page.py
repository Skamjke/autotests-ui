from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage
import re
from playwright.sync_api import Page,expect

class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.reg_form_component = RegistrationFormComponent(page)

        self.reg_button = Button(page, 'registration-page-registration-button', 'Registration button')
        self.login_link = Link(page, 'registration-page-login-link', 'Login link')

    def click_reg_button(self):
        self.reg_button.click()

    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(r".*/#/auth/login"))

