import re

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

class ToolbarComponent(BaseComponent):
    def __init__(self, page : Page):
        super().__init__(page)

        self.title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.button = page.get_by_test_id('courses-list-toolbar-create-course-button')

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Courses')

        expect(self.button).to_be_visible()

    def click_button(self):
        self.button.click()
        self.check_current_url(re.compile(r'.*/#/courses/create'))
