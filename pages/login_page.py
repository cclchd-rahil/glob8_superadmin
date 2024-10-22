from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN = (By.XPATH, "//button[contains(text(),'Login')]")
    FORGOT_PASSWORD = (By.XPATH, "//a[contains(text(),'Forgot Password?')]")
    REMEMBER_ME = (By.XPATH, "//body/div[@id='__next']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/label[1]/input[1]")

    def enter_email(self, email):
        self.send_keys(self.EMAIL, email)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN)

    def get_error_messages(self):
        messages = {}
        #Email validation
        try:
            email_error_element = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div/div/form/div[1]/div")
            messages['email'] = email_error_element.text
        except NoSuchElementException:
            messages['email'] = None  # or just don't add it if you prefer

        #Password validation
        try:
            password_error_element = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div/div/form/div[2]/div/div")
            messages['password'] = password_error_element.text
        except NoSuchElementException:
            messages['password'] = None  # or just don't add it if you prefer

        #Toaster
        try:
            require_error_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]"))
            )
            messages['require'] = require_error_element.text
        except (NoSuchElementException, TimeoutException):
            messages['require'] = None  # or skip this entry

        return messages