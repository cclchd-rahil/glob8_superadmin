import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class Transaction(BasePage):
    TRANSACTION = (By.XPATH, "//span[contains(text(),'Transaction')]")
    TITTLE = (By.XPATH, "//h2[contains(text(),'Transactions')]")

    def click_transaction(self):
        self.click(self.TRANSACTION)

    def get_transaction_title(self):
        transaction_title_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TITTLE)
        )
        return transaction_title_element.text



