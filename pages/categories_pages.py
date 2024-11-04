import pytest
from selenium.webdriver.common.by import By
from .base_page import BasePage

class Categories(BasePage):
    CATEGORIES = (By.XPATH, "//span[contains(text(),'Categories')]")
    TITTLE = (By.XPATH, "//h3[contains(text(),'Categories')]")

    def click_categories(self):
        self.click(self.CATEGORIES)

    def get_categories_title(self):
        transaction_title_element = self.driver.find_element(*self.TITTLE)
        return transaction_title_element.text
