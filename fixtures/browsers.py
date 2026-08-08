import pytest
from playwright.sync_api import sync_playwright, Page, Playwright
from _pytest.fixtures import SubRequest
import allure
from allure_commons.types import AttachmentType
from pages.authentication.registration_page import RegistrationPage
from tools.playwright.init_pages import initialization_playwright_page


@pytest.fixture(scope='function')
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialization_playwright_page(playwright, test_name=request.node.name)


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page)

    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_page.reg_form_component.fill('user.name@gmail.com','username','password')
    registration_page.click_reg_button()

    context.storage_state(path='browser-state.json')
    browser.close()

@pytest.fixture(scope='function')
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    yield from initialization_playwright_page(playwright, test_name=request.node.name, storage_state='browser-state.json')