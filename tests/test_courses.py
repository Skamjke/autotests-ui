import pytest
from playwright.sync_api import sync_playwright, expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):

        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        list_toolbar_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(list_toolbar_text).to_have_text('Courses')

        icon_folder = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_folder).to_be_visible()

        list_empty_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(list_empty_text).to_have_text('There is no results')

        list_description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(list_description_text).to_have_text('Results from the load test pipeline will be displayed here')




