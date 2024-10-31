from selenium.webdriver.common.by import By
from .base_page import BasePage


class Admin(BasePage):
    #Adding all locators

    ADMIN = (By.XPATH, "//span[contains(text(),'Admin Staff')]")
    ADDNEW = (By.XPATH, "/html/body/div/main/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/button")
    FIRSTNAME = (By.XPATH, "//input[@id='firstName']")
    LASTNAME = (By.XPATH, "//input[@id='lastName']")
    EMAIL = (By.XPATH, "//input[@id='email']")

    #Clicks, send keys, dropdowns
    def click_admin(self):
        self.click(self.ADMIN)

    def click_addnew(self):
        self.click(self.ADDNEW)

    def enter_firstname(self, firstname):
        self.send_keys(self.FIRSTNAME, firstname)

    def enter_lastname(self, lastname):
        self.send_keys(self.LASTNAME, lastname)

    def enter_email(self, email):
        self.send_keys(self.EMAIL, email)
