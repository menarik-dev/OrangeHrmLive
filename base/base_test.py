from pages.login_page import LoginPage
from pages.dashboard_page import DashBoardPage
from pages.profile_page import PersonalPage
from utils.Data import Data

class BaseTest:
    data: Data

    login_page: LoginPage
    dashboard_page: DashBoardPage
    personal_page: PersonalPage