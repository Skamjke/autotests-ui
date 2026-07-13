import pytest
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tests.authentication.test_registration import TestRegistration


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    @pytest.mark.parametrize('email, password',
                             [
                                 ('user.name@gmail.com', 'password'),
                                 ('user.name@gmail.com', '  '),
                                 ('  ', 'password')
                             ])
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

        login_page.login_form.check_visible()
        login_page.login_form.fill(email, password)

        login_page.click_login_button()

        login_page.check_wrong_email_or_password_alert_text()
        login_page.click_registration_link()

    def test_successful_authorization(self, login_page: LoginPage,registration_page: RegistrationPage, dashboard_page : DashboardPage):
        registration_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.reg_form_component.fill('user.name@gmail.com', 'username', 'password')
        registration_page.click_reg_button()

        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible('username')
        dashboard_page.sidebar.check_visible()


        dashboard_page.sidebar.click_logout()

        login_page.login_form.check_visible()

        login_page.login_form.fill('user.name@gmail.com', 'password')

        login_page.click_login_button()

        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible('username')
        dashboard_page.sidebar.check_visible()

    def test_navigate_from_authorization_to_registration(self, login_page: LoginPage, registration_page: RegistrationPage):
        login_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        login_page.click_registration_link()

        registration_page.reg_form_component.check_visible('','','')

        registration_page.click_login_link()

        login_page.login_form.check_visible()



