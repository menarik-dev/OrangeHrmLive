from utils.WaitUntil import WaitUntil

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.PAGE_URL)

    def is_opened(self):
        # WaitUntil.IsPageOpened(self.driver, timeout, url)
        pass