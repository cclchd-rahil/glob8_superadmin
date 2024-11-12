import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class SupportTickets(BasePage):
    SUPPORTTICKETS = (By.XPATH, "//span[contains(text(),'Support Ticket')]")
    TITTLE = (By.XPATH, "//h2[contains(text(),'Support Tickets')]")

    def click_support(self):
        self.click(self.SUPPORTTICKETS)

    def get_support_title(self):
        transaction_title_element =WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TITTLE)
        )
        return transaction_title_element.text
