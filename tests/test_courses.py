import pytest


from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage




@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_list_page.navbar.check_visible('username')

    courses_list_page.sidebar.check_visible()

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.empty_view.check_visible('There is no results','Results from the load test pipeline will be displayed here')



@pytest.mark.courses
@pytest.mark.regression
def test_create_course (create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

    create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
    create_course_page.image_upload.check_visible(is_image_uploaded=False)
    create_course_page.create_course_form.check_visible('', '', '', '0', '0')

    create_course_page.create_course_exercises_toolbar.check_visible()
    create_course_page.exercises_empty_view.check_visible('There is no exercises', 'Click on "Create exercise" button to create new exercise')

    create_course_page.image_upload.upload_preview_image('./testdata/files/image.png')
    create_course_page.image_upload.check_visible(is_image_uploaded=True)

    create_course_page.create_course_form.fill('Playwright','2 weeks','Playwright','100','10')
    create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=False)

    create_course_page.create_course_toolbar.click_create_course_button()

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible('Playwright','2 weeks','100','10',0)

