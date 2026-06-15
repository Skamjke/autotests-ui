import pytest

from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.regression
@pytest.mark.registration
def test_successfully_registration(chromium_page: Page):
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        reg_email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('//div//input')
        reg_email_input.fill('user.name@gmail.com')

        reg_username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('//div//input')
        reg_username_input.fill('username')

        reg_password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('//div//input')
        reg_password_input.fill('password')

        reg_button = chromium_page.get_by_test_id('registration-page-registration-button')
        reg_button.click()

        title_check = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
        expect(title_check).to_be_visible()