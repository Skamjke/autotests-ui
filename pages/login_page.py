from playwright.sync_api import Page,expect

from components.authentication.login_form_component import LoginFormComponent
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)

        self.button_login = page.get_by_test_id('login-page-login-button')
        self.wrong_email_or_password_alert_text = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
        self.registration_link = page.get_by_test_id('login-page-registration-link')

    def click_login_button(self):
        self.button_login.click()

    def click_registration_link(self):
        self.registration_link.click()

    def check_wrong_email_or_password_alert_text(self):
        expect(self.wrong_email_or_password_alert_text).to_be_visible()
        expect(self.wrong_email_or_password_alert_text).to_have_text('Wrong email or password')