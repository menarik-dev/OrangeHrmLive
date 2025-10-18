from base.base_page import BasePage
from utils.WaitUntil import WaitUntil
from utils.Links import Links
import allure

class DashBoardPage(BasePage):
    PAGE_URL = Links.DASHBOARD_PAGE

    # Locators
    MY_INFO_BUTTON =  ("xpath", "(//*[@class ='oxd-main-menu-item-wrapper'] // a)[6]")

    @allure.step("Go to profile...")
    def go_to_profile(self):
        return WaitUntil.ClickElement(self.driver, self.MY_INFO_BUTTON, 10)