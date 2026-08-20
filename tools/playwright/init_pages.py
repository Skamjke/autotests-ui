
from playwright.sync_api import Playwright,Page
import allure
from pytest_playwright.pytest_playwright import browser_type

from config import settings, Browser

def initialization_playwright_page(playwright: Playwright, test_name: str, browser_type: Browser, storage_state: str | None = None) -> Page:
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url(), storage_state=storage_state, record_video_dir='./videos')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    context.tracing.stop(path=f'./tracing/{test_name}.zip')
    browser.close()

    allure.attach.file(f'./tracing/{test_name}.zip', name='trace', extension='.zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)