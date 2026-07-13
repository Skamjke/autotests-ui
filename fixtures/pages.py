import pytest

from playwright.sync_api import Page

from fixtures.browsers import chromium_page_with_state
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    login_page = LoginPage(page=chromium_page)
    return login_page

@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    registration_page = RegistrationPage(page=chromium_page)
    return registration_page

@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    dashboard_page = DashboardPage(page=chromium_page)
    return dashboard_page

@pytest.fixture
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    courses_list_page = CoursesListPage(page=chromium_page_with_state)
    return courses_list_page

@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    create_course_page = CreateCoursePage(page=chromium_page_with_state)
    return create_course_page

@pytest.fixture
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
    dashboard_page_with_state = DashboardPage(page=chromium_page_with_state)
    return dashboard_page_with_state