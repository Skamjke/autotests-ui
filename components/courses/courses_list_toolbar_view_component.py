import re

import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.button import Button
from elements.text import Text

class ToolbarComponent(BaseComponent):
    def __init__(self, page : Page):
        super().__init__(page)

        self.title = Text(page,'courses-list-toolbar-title-text', 'Title')
        self.button = Button(page, 'courses-list-toolbar-create-course-button', 'Button')
    @allure.step('Check visible create toolbar on courses list')
    def check_visible(self):
        self.title.check_visible()
        self.title.have_text('Courses')

        self.button.check_visible()

    def click_button(self):
        self.button.click()
        self.check_current_url(re.compile(r'.*/#/courses/create'))
