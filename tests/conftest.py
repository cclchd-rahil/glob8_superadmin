import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.fixture(scope="session")
# def driver():
#     driver = webdriver.Chrome()
#
#     yield driver
#     driver.quit()

def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    return driver

BASE_URL = "https://admin.nfttrace.com/login"
USERNMAE = "superadmin@gmail.com"
PASSWORD = "Admin@123"

@pytest.fixture(scope="session")
def login(driver):
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.enter_email(USERNMAE)
    login_page.enter_password(PASSWORD)
    login_page.click_login()
    yield
