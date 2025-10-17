from base.base_page import BasePage
from utils.WaitUntil import WaitUntil
from utils.Links import Links

class DashBoardPage(BasePage):
    PAGE_URL = Links.DASHBOARD_PAGE

    # Locators
    MY_INFO_BUTTON =  ("xpath", "(//*[@class ='oxd-main-menu-item-wrapper'] // a)[6]")

    def go_to_profile(self):
        return WaitUntil.ClickElement(self.driver, self.MY_INFO_BUTTON, 10)