import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.input import Input
from elements.textarea import TextArea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.input_title = Input(page,'create-course-form-title-input', 'Input title')
        self.input_estimated_time = Input(page,'create-course-form-estimated-time-input', 'Input estimated time')
        self.textarea_description = TextArea(page,'create-course-form-description-input','Textarea description')
        self.input_max_score = Input(page,'create-course-form-max-score-input', 'Input max score')
        self.input_min_score = Input(page,'create-course-form-min-score-input', 'Input min score')

    @allure.step('Check visible create course form')
    def check_visible(self, title: str, estimated_time : str, description: str, max_score : str, min_score : str):
        self.input_title.check_visible()
        self.input_title.check_have_value(title)

        self.input_estimated_time.check_visible()
        self.input_estimated_time.check_have_value(estimated_time)

        self.textarea_description.check_visible()
        self.textarea_description.check_have_value(description)

        self.input_max_score.check_visible()
        self.input_max_score.check_have_value(max_score)

        self.input_min_score.check_visible()
        self.input_min_score.check_have_value(min_score)

    @allure.step('Fill create course form')
    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.input_title.fill(title)
        self.input_title.check_have_value(title)

        self.input_estimated_time.fill(estimated_time)
        self.input_estimated_time.check_have_value(estimated_time)

        self.textarea_description.fill(description)
        self.textarea_description.check_have_value(description)

        self.input_max_score.fill(max_score)
        self.input_max_score.check_have_value(max_score)

        self.input_min_score.fill(min_score)
        self.input_min_score.check_have_value(min_score)