from utils.WaitUntil import WaitUntil
from allure_commons.types import AttachmentType
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            WaitUntil.IsPageOpened(self.driver, 10, self.PAGE_URL)

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body= self.driver.get_screenshot_as_png(),
            name= screenshot_name,
            attachment_type= AttachmentType.PNG
        )