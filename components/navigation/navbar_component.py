from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text
import allure

class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar_title = Text(page, 'navigation-navbar-app-title-text', 'Title')
        self.navbar_welcome_title = Text(page,'navigation-navbar-welcome-title-text','Welcome title')

    @allure.step('Check visible navigation bar for user "{username}"')
    def check_visible(self, username: str):
        self.navbar_title.check_visible()
        self.navbar_title.have_text('UI Course')

        self.navbar_welcome_title.check_visible()
        self.navbar_welcome_title.have_text(f'Welcome, {username}!')