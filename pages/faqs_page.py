import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class Faqs(BasePage):
    FAQS = (By.XPATH, "//span[contains(text(),'FAQ')]")
    TITTLE = (By.XPATH, "//h2[contains(text(),'FAQs')]")

    def click_faqs(self):
        self.click(self.FAQS)

    def get_faqs_title(self):
        faqs_title_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TITTLE)
        )
        return faqs_title_element.text
