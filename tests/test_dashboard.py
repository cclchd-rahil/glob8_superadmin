import pytest
from selenium.webdriver.common.by import By
from pages import login_page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.usefixtures("login")
def test_admin_click(driver):
    dashboard_page = DashboardPage(driver)
    dashboard_page.click_admin()







