from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class DashboardPage(BasePage):
    TOTALADMIN = (By.XPATH, "//h4[contains(text(),'Total Admins')]")

    def click_totaladmin(self):
        self.click(self.TOTALADMIN)

