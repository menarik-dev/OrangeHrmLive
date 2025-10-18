from base.base_test import BaseTest
import allure
import pytest

@allure.feature("Profile functionality")
class TestProfileFeature(BaseTest):
    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_name(self, driver):
        self.login_page.open()
        self.login_page.Login(login=self.data.LOGIN, password=self.data.PASSWORD)
        self.dashboard_page.is_opened()
        self.dashboard_page.go_to_profile()
        self.personal_page.change_name(self.data.NEW_NAME)
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved()
