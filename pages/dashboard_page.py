from selenium.webdriver.common.by import By
from .base_page import BasePage


class DashboardPage(BasePage):
    ADMIN = (By.XPATH, "//span[contains(text(),'Admin Staff')]")

    def click_admin(self):
        self.click(self.ADMIN)
