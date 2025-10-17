from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUntil():
    @staticmethod
    def WaitPageLoaded(webdriver, timeInSeconds):
        if (timeInSeconds > 0):
            (WebDriverWait(webdriver, timeInSeconds)
             .until(lambda driver: driver.execute_script("return document.readyState === 'complete'"))
             )

    @staticmethod
    def WaitElementVisible(webdriver, locator, timeOutInSeconds):
        return WebDriverWait(webdriver, timeOutInSeconds).until(EC.visibility_of_element_located(locator))

    @staticmethod
    def WaitElementClickable(webdriver, locator, timeOutInSeconds):
        return WebDriverWait(webdriver, timeOutInSeconds).until(EC.element_to_be_clickable(locator))

    @staticmethod
    def InputText(webdriver, locator, text, timeOutInSeconds=10):
        element = WaitUntil.WaitElementVisible(webdriver, locator, timeOutInSeconds)
        element.clear()
        element.send_keys(text)

    @staticmethod
    def ClickElement(webdriver, locator, timeOutInSeconds=10):
        element = WaitUntil.WaitElementClickable(webdriver, locator, timeOutInSeconds)
        element.click()

    @staticmethod
    def IsElementVisible(webdriver, locator, timeOutInSeconds=10):
        try:
            WaitUntil.WaitElementVisible(webdriver, locator, timeOutInSeconds)
            return True
        except Exception as _ex:
            print(_ex)
            return False

    @staticmethod
    def GetElementText(webdriver, locator, timeOutInSeconds):
        element = WaitUntil.WaitElementVisible(webdriver, locator, timeOutInSeconds)
        return element.text