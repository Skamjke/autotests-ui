from playwright.sync_api import Page,expect
from typing import Pattern

class BasePage():
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url, wait_until="networkidle")

    def page_timeout(self, ms: int):
        self.page.wait_for_timeout(ms)

    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)

