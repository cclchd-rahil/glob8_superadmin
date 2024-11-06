import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class Categories(BasePage):
    CATEGORIES = (By.XPATH, "//span[contains(text(),'Categories')]")
    TITTLE = (By.XPATH, "//h3[contains(text(),'Categories')]")

    def click_categories(self):
        self.click(self.CATEGORIES)

    def get_categories_title(self):
        categories_title_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TITTLE)
        )
        return categories_title_element.text
