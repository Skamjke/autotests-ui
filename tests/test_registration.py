import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.reg_form_component.fill('user.name@gmail.com', 'username', 'password')
        registration_page.click_reg_button()
        dashboard_page.dashboard_toolbar.check_visible()