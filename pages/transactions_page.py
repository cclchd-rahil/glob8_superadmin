import pytest
from selenium.webdriver.common.by import By
from .base_page import BasePage

class Transaction(BasePage):
    TRANSACTION = (By.XPATH, "//span[contains(text(),'Transaction')]")
    TITTLE = (By.XPATH, "//h2[contains(text(),'Transactions')]")

    def click_transaction(self):
        self.click(self.TRANSACTION)

    def get_transaction_title(self):
        transaction_title_element = self.driver.find_element(*self.TITTLE)
        return transaction_title_element.text



