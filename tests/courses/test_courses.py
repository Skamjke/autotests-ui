import pytest
from allure_commons.types import Severity
from tools.allure.tags import AllureTags
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
import allure
from tools.allure.epics import AllureEpics
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory

@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTags.REGRESSIONS, AllureTags.COURSES)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page.navbar.check_visible('username')

        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title('Create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible('', '', '', '0', '0')

        create_course_page.create_course_exercises_toolbar.check_visible()
        create_course_page.exercises_empty_view.check_visible('There is no exercises',
                                                              'Click on "Create exercise" button to create new exercise')

        create_course_page.image_upload.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload.check_visible(is_image_uploaded=True)

        create_course_page.create_course_form.fill('Playwright', '2 weeks', 'Playwright', '100', '10')
        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=False)

        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible('Playwright', '2 weeks', '100', '10', 0)

    @allure.title('Edit course')
    @allure.severity(Severity.NORMAL)
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page.image_upload.upload_preview_image('./testdata/files/image.png')
        create_course_page.create_course_form.fill('Playwright', '2 weeks', 'Playwright', '100', '10')

        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.course_view.check_visible('Playwright', '2 weeks', '100', '10', 0)

        courses_list_page.courses_view_menu.click_edit_button(0)

        create_course_page.create_course_form.fill('Playwright_new', '4 weeks', 'Playwright_new', '200', '20')
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.course_view.check_visible('Playwright_new', '4 weeks', '200', '20', 0)


