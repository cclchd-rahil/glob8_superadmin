import selectors
import time

from selenium.common import NoSuchElementException, TimeoutException

from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Admin(BasePage):
    # Adding all locators
    ADMIN = (By.XPATH, "//span[contains(text(),'Admin Staff')]")
    ADDNEW = (By.XPATH, "/html/body/div/main/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/button")
    FIRSTNAME = (By.XPATH, "//input[@id='firstName']")
    LASTNAME = (By.XPATH, "//input[@id='lastName']")
    MOBILENUMBER = (By.ID, "number")
    EMAIL = (By.XPATH, "//input[@id='email']")
    ROLE = (By.ID, "role")
    PASSWORD = (By.ID, "password")
    CPASSWORD = (By.ID, "confirmPassword")
    SUBMIT = (By.XPATH, "//button[contains(text(),'Submit')]")

    # Clicks, send keys, dropdowns
    def click_admin(self):
        self.click(self.ADMIN)

    def click_addnew(self):
        # Wait for the button to be clickable, with a fallback screenshot for debugging
        try:
            add_new_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.ADDNEW)
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", add_new_button)
            add_new_button.click()
        except Exception as e:
            self.driver.save_screenshot("click_addnew_error.png")  # Save a screenshot if an error occurs
            raise e

    def enter_firstname(self, firstname):
        self.send_keys(self.FIRSTNAME, firstname)

    def enter_lastname(self, lastname):
        self.send_keys(self.LASTNAME, lastname)

    def enter_mobilenumber(self, mobilenumber):
        self.send_keys(self.MOBILENUMBER, mobilenumber)

    def enter_email(self, email):
        self.send_keys(self.EMAIL, email)

    def select_role_by_index(self, index):
        role_dropdown = self.driver.find_element(*self.ROLE)
        select = Select(role_dropdown)
        select.select_by_index(index)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    def enter_cpassword(self, cpassword):
        self.send_keys(self.CPASSWORD, cpassword)

    def click_submit(self):
        # Locate the submit button and scroll to it
        submit = self.driver.find_element(*self.SUBMIT)
        self.driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

    def get_toaster_messages(self):
        messages = {}

        try:
            require_success_element = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'User created successfully!')]"))
            )
            messages['require'] = require_success_element.text
        except (NoSuchElementException, TimeoutException):
            messages['require'] = None  # If not found, set to None

            # Check for error message if the success message was not found
        if messages['require'] is None:
            try:
                error_element = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//div[contains(text(),'Email or mobile already exists')]"))
                )
                messages['error'] = error_element.text  # Store the error message
            except (NoSuchElementException, TimeoutException):
                messages['error'] = None  # If not found, set to None

        return messages







