from components.base_component import BaseComponent
from playwright.sync_api import Page, expect



class CreateCourseExerciseFormComponent(BaseComponent):
    def check_visible(self, index: int, title: str, description: str):
        subtitle = self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')
        input_title = self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input').locator('input')
        input_description = self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input').locator('input')

        expect(subtitle).to_be_visible()
        expect(subtitle).to_have_text(f'#{index + 1} Exercise')

        expect(input_title).to_be_visible()
        expect(input_title).to_have_value(title)

        expect(input_description).to_be_visible()
        expect(input_description).to_have_value(description)
        expect(self.exercises_create_button).to_be_visible()


    def click_delete_button(self, index: int):
        delete_button = self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-delete-exercise-button')
        delete_button.click()

    def fill_exercises_form(self, index: int, title: str, description: str):
        input_title = self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input').locator('input')
        input_description = self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input').locator('input')

        input_title.fill(title)
        expect(input_title).to_have_value(title)

        input_description.fill(description)
        expect(input_description).to_have_value(description)