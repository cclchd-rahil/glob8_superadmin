import pytest
from selenium.webdriver.common.by import By
from .base_page import BasePage

class Faqs(BasePage):
    FAQS = (By.XPATH, "//span[contains(text(),'FAQ')]")
    TITTLE = (By.XPATH, "//h2[contains(text(),'FAQs')]")

    def click_faqs(self):
        self.click(self.FAQS)

    def get_faqs_title(self):
        transaction_title_element = self.driver.find_element(*self.TITTLE)
        return transaction_title_element.text
