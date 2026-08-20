import pytest

from playwright.sync_api import Page

from fixtures.browsers import page_with_state
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login_page = LoginPage(page=page)
    return login_page

@pytest.fixture
def registration_page(page: Page) -> RegistrationPage:
    registration_page = RegistrationPage(page=page)
    return registration_page

@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    dashboard_page = DashboardPage(page=page)
    return dashboard_page

@pytest.fixture
def courses_list_page(page_with_state: Page) -> CoursesListPage:
    courses_list_page = CoursesListPage(page=page_with_state)
    return courses_list_page

@pytest.fixture
def create_course_page(page_with_state: Page) -> CreateCoursePage:
    create_course_page = CreateCoursePage(page=page_with_state)
    return create_course_page

@pytest.fixture
def dashboard_page_with_state(page_with_state: Page) -> DashboardPage:
    dashboard_page_with_state = DashboardPage(page=page_with_state)
    return dashboard_page_with_state