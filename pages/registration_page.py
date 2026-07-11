from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page,expect

class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.reg_form_component = RegistrationFormComponent(page)

        self.reg_button = page.get_by_test_id('registration-page-registration-button')


    def click_reg_button(self):
        self.reg_button.click()

