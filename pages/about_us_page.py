from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AboutUs(BasePage):
    ABOUTUS = (By.XPATH, "//span[contains(text(),'About Us')]")
    TITTLE = (By.XPATH, "//a[contains(text(),'About NFTtrace')]")

    def click_about_us(self):
        self.click(self.ABOUTUS)

    def get_tittle_element(self):
        about_us_tittle = self.driver.find_element(*self.TITTLE)
        return about_us_tittle.text

