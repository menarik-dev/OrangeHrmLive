from base.base_page import BasePage
from utils.Links import Links
from selenium.webdriver import Keys

from utils.WaitUntil import WaitUntil


class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    # SURNAME_FIELD = ("xpath", "//input[@name='firstName']")
    # FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def change_name(self, new_name):
        first_name_field = WaitUntil.WaitElementClickable(self.driver, self.FIRST_NAME_FIELD, 10)
        first_name_field.clear()
        first_name_field.send_keys(Keys.COMMAND + "A")
        first_name_field.send_keys(new_name)
        self.new_name = new_name

    def save_changes(self):
        return WaitUntil.ClickElement(self.driver, self.SAVE_BUTTON, 10)

    def is_changes_saved(self):
        pass