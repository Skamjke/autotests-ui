from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.input_title = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.input_estimated_time = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        self.textarea_description = page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        self.input_max_score = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.input_min_score = page.get_by_test_id('create-course-form-min-score-input').locator('input')

    def check_visible(self, title: str, estimated_time : str, description: str, max_score : str, min_score : str):
        expect(self.input_title).to_be_visible()
        expect(self.input_title).to_have_value(title)

        expect(self.input_estimated_time).to_be_visible()
        expect(self.input_estimated_time).to_have_value(estimated_time)

        expect(self.textarea_description).to_be_visible()
        expect(self.textarea_description).to_have_value(description)

        expect(self.input_max_score).to_be_visible()
        expect(self.input_max_score).to_have_value(max_score)

        expect(self.input_min_score).to_be_visible()
        expect(self.input_min_score).to_have_value(min_score)

    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.input_title.fill(title)
        expect(self.input_title).to_have_value(title)

        self.input_estimated_time.fill(estimated_time)
        expect(self.input_estimated_time).to_have_value(estimated_time)

        self.textarea_description.fill(description)
        expect(self.textarea_description).to_have_value(description)

        self.input_max_score.fill(max_score)
        expect(self.input_max_score).to_have_value(max_score)

        self.input_min_score.fill(min_score)
        expect(self.input_min_score).to_have_value(min_score)
