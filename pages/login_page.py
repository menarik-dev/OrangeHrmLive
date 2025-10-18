from base.base_page import BasePage
from utils.WaitUntil import WaitUntil
from utils.Links import Links
import allure

class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    # Locators
    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")
    # ERROR_MESSAGE = ("xpath", "//div[@role='alert']")
    # EXPECTED_ERROR_MESSAGE = "Invalid credentials"

    @allure.step("Log in to site")
    def Login(self, login, password):
        WaitUntil.InputText(self.driver, self.USERNAME_FIELD, login, 10  )
        WaitUntil.InputText(self.driver, self.PASSWORD_FIELD, password, 10  )
        WaitUntil.ClickElement(self.driver, self.SUBMIT_BUTTON, 10)