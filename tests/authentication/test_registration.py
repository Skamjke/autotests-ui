import pytest
import allure
from tools.allure.tags import AllureTags
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from tools.allure.epics import AllureEpics
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

from tools.route import AppRoute
from config import settings


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTags.REGISTRATION, AllureTags.REGRESSIONS)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.title('Registration with correct email, username and password')
    @allure.severity(Severity.BLOCKER)
    def test_successful_registration(self,registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.reg_form_component.fill(settings.test_user.email, settings.test_user.username, settings.test_user.password)
        registration_page.click_reg_button()
        dashboard_page.dashboard_toolbar.check_visible()
