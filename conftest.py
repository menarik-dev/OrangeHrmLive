import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.dashboard_page import DashBoardPage
from pages.login_page import LoginPage
from pages.profile_page import PersonalPage
from utils.Data import Data


@pytest.fixture(scope="class", autouse=True)
def driver(request):
    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver

    driver.quit()

@pytest.fixture(autouse=True)
def setup(request, driver):
    request.cls.driver = driver
    request.cls.data = Data()
    request.cls.login_page = LoginPage(driver)
    request.cls.dashboard_page = DashBoardPage(driver)
    request.cls.personal_page = PersonalPage(driver)