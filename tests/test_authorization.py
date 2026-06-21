import pytest
from playwright.sync_api import sync_playwright, expect, Page


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize('email, password',
                         [('user.name@gmail.com', 'password'), ('user.name@gmail.com', '  '), ('  ', 'password')])
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    input_email = chromium_page.get_by_test_id('login-form-email-input').locator('//div//input')
    input_email.fill(email)

    input_password = chromium_page.get_by_test_id('login-form-password-input').locator('//div//input')
    input_password.fill(password)

    button_login = chromium_page.get_by_test_id('login-page-login-button')
    button_login.click()

    wrong_email_or_password_alert = chromium_page.locator(
        '//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')

    chromium_page.wait_for_timeout(5000)
