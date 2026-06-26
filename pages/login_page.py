from playwright.sync_api import Page,expect

from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.input_email = page.get_by_test_id('login-form-email-input').locator('//div//input')
        self.input_password = page.get_by_test_id('login-form-password-input').locator('//div//input')
        self.button_login = page.get_by_test_id('login-page-login-button')
        self.wrong_email_or_password_alert_text = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
        self.registration_link = page.get_by_test_id('login-page-registration-link')

    def fill_login_form(self, email: str, password: str):
        self.input_email.fill(email)
        expect(self.input_email).to_have_value(email)
        self.input_password.fill(password)
        expect(self.input_password).to_have_value(password)

    def click_login_button(self):
        self.button_login.click()

    def click_registration_link(self):
        self.registration_link.click()

    def check_wrong_email_or_password_alert_text(self):
        expect(self.wrong_email_or_password_alert_text).to_be_visible()
        expect(self.wrong_email_or_password_alert_text).to_have_text('Wrong email or password')