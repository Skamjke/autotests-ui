from playwright.sync_api import sync_playwright, Page, Playwright
import pytest

@pytest.fixture(autouse=False, scope='session')
def initialize_browser_state(playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        reg_email_input = page.get_by_test_id('registration-form-email-input').locator('//div//input')
        reg_email_input.fill('user.name@gmail.com')

        reg_username_input = page.get_by_test_id('registration-form-username-input').locator('//div//input')
        reg_username_input.fill('username')

        reg_password_input = page.get_by_test_id('registration-form-password-input').locator('//div//input')
        reg_password_input.fill('password')

        reg_button = page.get_by_test_id('registration-page-registration-button')
        reg_button.click()

        context.storage_state(path='browser-state.json')

def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
