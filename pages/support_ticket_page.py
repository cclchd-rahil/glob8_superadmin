import pytest
from selenium.webdriver.common.by import By
from .base_page import BasePage

class SupportTickets(BasePage):
    SUPPORTTICKETS = (By.XPATH, "//span[contains(text(),'Support Ticket')]")
    TITTLE = (By.XPATH, "//h2[contains(text(),'Support Tickets')]")

    def click_support(self):
        self.click(self.SUPPORTTICKETS)

    def get_support_title(self):
        transaction_title_element = self.driver.find_element(*self.TITTLE)
        return transaction_title_element.text
