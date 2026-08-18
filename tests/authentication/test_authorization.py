import pytest
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpics
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
import allure
from allure_commons.types import Severity
from config import settings
from tools.route import AppRoute


@pytest.mark.regression
@pytest.mark.authorization
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @pytest.mark.parametrize('email, password',
                             [
                                 ('user.name@gmail.com', 'password'),
                                 ('user.name@gmail.com', '  '),
                                 ('  ', 'password')
                             ])
    @allure.tag(AllureTags.AUTHORIZATION, AllureTags.REGRESSIONS)
    @allure.title("User login with wrong email or password")
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit(AppRoute.LOGIN)
        
        login_page.login_form.check_visible()
        login_page.login_form.fill(email, password)

        login_page.click_login_button()

        login_page.check_wrong_email_or_password_alert_text()
        login_page.click_registration_link()

    @allure.tag(AllureTags.USER_LOGIN)
    @allure.title("User login with correct email and password")
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(self, login_page: LoginPage,registration_page: RegistrationPage, dashboard_page : DashboardPage):
        registration_page.visit(AppRoute.REGISTRATION)

        registration_page.reg_form_component.fill(settings.test_user.email, settings.test_user.username, settings.test_user.password)
        registration_page.click_reg_button()

        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()


        dashboard_page.sidebar.click_logout()

        login_page.login_form.check_visible()

        login_page.login_form.fill(settings.test_user.email, settings.test_user.password)

        login_page.click_login_button()

        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()

    @allure.tag(AllureTags.NAVIGATION)
    @allure.title("Navigation from login page to registration page")
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(self, login_page: LoginPage, registration_page: RegistrationPage):
        login_page.visit(AppRoute.LOGIN)

        login_page.click_registration_link()

        registration_page.reg_form_component.check_visible('','','')

        registration_page.click_login_link()

        login_page.login_form.check_visible()



