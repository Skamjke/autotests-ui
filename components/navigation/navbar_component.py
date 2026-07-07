from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar_title = page.get_by_test_id('navigation-navbar-app-title-text')
        self.navbar_welcome_title = page.get_by_test_id('navigation-navbar-welcome-title-text')

    def check_visible(self, username: str):
        expect(self.navbar_title).to_be_visible()
        expect(self.navbar_title).to_have_text('UI Course')

        expect(self.navbar_welcome_title).to_be_visible()
        expect(self.navbar_welcome_title).to_have_text(f'Welcome, {username}!')