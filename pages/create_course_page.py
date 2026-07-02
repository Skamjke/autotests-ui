from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_create_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        self.preview_image = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')
        self.preview_empty_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.preview_empty_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.preview_empty_description = page.get_by_test_id('create-course-preview-empty-view-description-text')

        self.image_upload_view_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.image_upload_view_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.image_upload_view_description = page.get_by_test_id('create-course-preview-image-upload-widget-info-description-text')
        self.image_upload_view_button = page.get_by_test_id('create-course-preview-image-upload-widget-upload-button')
        self.image_upload_view_input = page.get_by_test_id('create-course-preview-image-upload-widget-input')
        self.image_upload_remove_view_button = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')

        self.create_course_input_title = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.create_course_input_estimated_time = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        self.create_course_textarea_description = page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        self.create_course_input_max_score = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.create_course_input_min_score = page.get_by_test_id('create-course-form-min-score-input').locator('input')

        self.exercises_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.exercises_empty_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.exercises_empty_title = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        self.exercises_empty_description = page.get_by_test_id('create-course-exercises-empty-view-description-text')
        self.exercises_create_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')

    def check_visible_create_course_description(self):
        expect(self.create_course_create_button).to_be_visible()

    def check_disabled_create_course_button(self):
        expect(self.create_course_create_button).to_be_disabled()

    def click_create_course_button(self):
        self.create_course_create_button.click()


    def check_visible_preview_empty(self):
        expect(self.preview_empty_icon).to_be_visible()

        expect(self.preview_empty_title).to_be_visible()
        expect(self.preview_empty_title).to_have_text('No image selected')

        expect(self.preview_empty_description).to_be_visible()
        expect(self.preview_empty_description).to_have_text('Preview of selected image will be displayed here')

    def check_visible_image_upload_view(self, is_image_uploaded: bool = False):
        expect(self.image_upload_view_icon).to_be_visible()

        expect(self.image_upload_view_title).to_be_visible()
        expect(self.image_upload_view_title).to_have_text('Tap on "Upload image" button to select file')

        expect(self.image_upload_view_description).to_be_visible()
        expect(self.image_upload_view_description).to_have_text('Recommended file size 540X300')

        expect(self.image_upload_view_button).to_be_visible()

        if is_image_uploaded:
            expect(self.image_upload_remove_view_button).to_be_visible()

    def click_image_upload_remove_button(self):
        self.image_upload_remove_view_button.click()

    def check_visible_preview_image(self):
        expect(self.preview_image).to_be_visible()

    def upload_preview_image(self, file: str):
        self.image_upload_view_input.set_input_files(file)

    def check_visible_create_course_form(self, title: str, estimated_time : str, description: str, max_score : str, min_score : str):
        expect(self.create_course_input_title).to_be_visible()
        expect(self.create_course_input_title).to_have_value(title)

        expect(self.create_course_input_estimated_time).to_be_visible()
        expect(self.create_course_input_estimated_time).to_have_value(estimated_time)

        expect(self.create_course_textarea_description).to_be_visible()
        expect(self.create_course_textarea_description).to_have_value(description)

        expect(self.create_course_input_max_score).to_be_visible()
        expect(self.create_course_input_max_score).to_have_value(max_score)

        expect(self.create_course_input_min_score).to_be_visible()
        expect(self.create_course_input_min_score).to_have_value(min_score)

    def fill_create_course_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.create_course_input_title.fill(title)
        expect(self.create_course_input_title).to_have_value(title)

        self.create_course_input_estimated_time.fill(estimated_time)
        expect(self.create_course_input_estimated_time).to_have_value(estimated_time)

        self.create_course_textarea_description.fill(description)
        expect(self.create_course_textarea_description).to_have_value(description)

        self.create_course_input_max_score.fill(max_score)
        expect(self.create_course_input_max_score).to_have_value(max_score)

        self.create_course_input_min_score.fill(min_score)
        expect(self.create_course_input_min_score).to_have_value(min_score)

    def check_visible_exercises_title(self):
        expect(self.exercises_title).to_be_visible()
        expect(self.exercises_title).to_have_text('Exercises')

    def check_visible_empty_view_exercises(self):
        expect(self.exercises_empty_icon).to_be_visible()

        expect(self.exercises_empty_title).to_be_visible()
        expect(self.exercises_empty_title).to_have_text('There is no exercises')

        expect(self.exercises_empty_description).to_be_visible()
        expect(self.exercises_empty_description).to_have_text('Click on "Create exercise" button to create new exercise')

    def check_visible_exercises_create_button(self):
        expect(self.exercises_create_button).to_be_visible()

    def click_exercises_create_button(self):
        self.exercises_create_button.click()

    def check_visible_delete_button(self, index: int):
        expect(self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-delete-exercise-button')).to_be_visible()

    def click_exercises_delete_button(self, index : int):
        delete_exercises_button = self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-delete-exercise-button')
        delete_exercises_button.click()

    def check_visible_exercises_form(self, index: int, title: str, description: str):
        exercises_subtitle = self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')
        exercises_input_title = self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input').locator('input')
        exercises_input_description = self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input').locator('input')

        expect(exercises_subtitle).to_be_visible()
        expect(exercises_subtitle).to_have_text(f'#{index + 1} Exercise')

        expect(exercises_input_title).to_be_visible()
        expect(exercises_input_title).to_have_value(title)

        expect(exercises_input_description).to_be_visible()
        expect(exercises_input_description).to_have_value(description)

    def fill_exercises_form(self, index: int, title: str, description: str):
        exercises_input_title = self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input').locator('input')
        exercises_input_description = self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input').locator('input')

        exercises_input_title.fill(title)
        expect(exercises_input_title).to_have_value(title)

        exercises_input_description.fill(description)
        expect(exercises_input_description).to_have_value(description)




