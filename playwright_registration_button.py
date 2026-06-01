from time import sleep

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    reg_button = page.get_by_test_id('registration-page-registration-button')
    expect(reg_button).to_be_disabled()

    reg_email_input = page.get_by_test_id('registration-form-email-input').locator('//div//input')
    reg_email_input.fill('user.name@gmail.com')

    reg_username_input = page.get_by_test_id('registration-form-username-input').locator('//div//input')
    reg_username_input.fill('username')

    reg_password_input = page.get_by_test_id('registration-form-password-input').locator('//div//input')
    reg_password_input.fill('password')

    expect(reg_button).to_be_enabled()

