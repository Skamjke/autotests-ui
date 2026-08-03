from playwright.sync_api import Page,expect
import re

from components.authentication.login_form_component import LoginFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
import allure



class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)


        self.button_login = Button(page,'login-page-login-button', 'Login')
        self.wrong_email_or_password_alert_text = Text(page,'login-page-wrong-email-or-password-alert', 'Wrong email or password')
        self.registration_link = Link(page,'login-page-registration-link','Registration')

    def click_login_button(self):
        self.button_login.click()

    def click_registration_link(self):
        self.registration_link.click()
        self.check_current_url(re.compile(r".*/#/auth/registration"))

    @allure.step('Check visible wrong email or password alert')
    def check_wrong_email_or_password_alert_text(self):
        self.wrong_email_or_password_alert_text.check_visible()
        self.wrong_email_or_password_alert_text.have_text('Wrong email or password')