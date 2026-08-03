from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.button import Button
from elements.text import Text

from elements.input import Input
import allure

class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.subtitle = Text(page,'create-course-exercise-{index}-box-toolbar-subtitle-text', 'Subtitle')
        self.input_title = Input(page,'create-course-exercise-form-title-{index}-input', 'Input title')
        self.input_description = Input(page,'create-course-exercise-form-description-{index}-input', 'Input description')
        self.delete_button_exercise = Button(page,'create-course-exercise-{index}-box-toolbar-delete-exercise-button', 'Delete exercise')

    @allure.step('Check visible exercise form at index "{index}"')
    def check_visible(self, index: int, title: str, description: str):

        self.subtitle.check_visible()
        self.subtitle.have_text(f'#{index + 1} Exercise', index=index)

        self.input_title.check_visible()
        self.input_title.check_have_value(title, index=index)

        self.input_description.check_visible()
        self.input_description.check_have_value(description, index=index)

    def click_delete_button(self, index: int):
        self.delete_button_exercise.click(index=index)

    def fill_exercises_form(self,index: int, title: str, description: str):
        self.input_title.fill(title, index=index)
        self.input_title.check_have_value(title, index=index)

        self.input_description.fill(description, index=index)
        self.input_description.check_have_value(description, index=index)