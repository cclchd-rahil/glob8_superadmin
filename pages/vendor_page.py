from selenium.common import NoSuchElementException, TimeoutException

from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Vendor(BasePage):
    # Adding all the locators
    VENDOR = (By.XPATH, "//span[contains(text(),'Vendor')]")
    ADDNEW = (By.XPATH, "//button[contains(text(),'+ Add New')]")
    ORGNAME = (By.XPATH, "//body/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]")
    PAN = (By.NAME, "pan")
    DESCRIPTION = (By.NAME, "description")
    GSTIN = (By.NAME, "gstin")
    ADDRESS = (By.NAME, "address")
    LOGO = (By.ID, "logo")
    NEXTBTN = (By.XPATH, "//button[contains(text(),'Next')]")
    ACCOUNTHOLDERNAME = (By.NAME, "accountHolderName")
    ACCOUNTNUMBER = (By.NAME, "accountNumber")
    BANKNAME = (By.NAME, "bankName")
    BRANCHNAME = (By.NAME, "branchName")
    IFSCCODE = (By.NAME, "ifscCode")
    BACKBTN = (By.XPATH, "//button[contains(text(),'Back')]")
    FIRSTNAME = (By.NAME, "firstName")
    LASTNAME = (By.NAME, "lastName")
    MOBILE = (By.NAME, "mobile")
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    CPASSWORD = (By.NAME, "reenterPassword")
    SUBMIT = (By.XPATH, "//button[contains(text(),'Submit')]")
    SUCCESS_TOASTER = (By.XPATH, "//div[contains(text(),'Vendor created successfully!')]")
    ERROR_1 = (By.XPATH, "//div[contains(text(),'Email already in use')]")
    ERROR_2 = (By.XPATH, "//div[contains(text(),'Mobile already in use')]")
    ERROR_3 = (By.XPATH, "//div[contains(text(),'GSTIN already in use')]")
    ERROR_4 = (By.XPATH, "//div[contains(text(),'PAN already in use')]")
    ERROR_5 = (By.XPATH, "//div[contains(text(),'Account Number already in use')]")

    #Functions
    def click_vendor(self):
        self.click(self.VENDOR)

    def click_addnew(self):
        self.click(self.ADDNEW)

    def enter_orgname(self, orgname):
        self.send_keys(self.ORGNAME, orgname)

    def enter_pan(self, pan):
        self.send_keys(self.PAN, pan)

    def enter_description(self, description):
        self.send_keys(self.DESCRIPTION, description)

    def enter_gstin(self, gstin):
        self.send_keys(self.GSTIN, gstin)

    def enter_address(self, address):
        self.send_keys(self.ADDRESS, address)

    def upload_logo(self, logo):
        self.send_keys(self.LOGO, logo)

    def click_next(self):
        self.click(self.NEXTBTN)

    def enter_holdername(self, holdername):
        self.send_keys(self.ACCOUNTHOLDERNAME, holdername)

    def enter_accountnumber(self, accountnumber):
        self.send_keys(self.ACCOUNTNUMBER, accountnumber)

    def enter_bankname(self, bankname):
        self.send_keys(self.BANKNAME, bankname)

    def enter_branchname(self, branchname):
        self.send_keys(self.BRANCHNAME, branchname)

    def enter_ifsccode(self, ifsccode):
        self.send_keys(self.IFSCCODE, ifsccode)

    def enter_firstname(self, firstname):
        self.send_keys(self.FIRSTNAME, firstname)

    def enter_lastname(self, lastname):
        self.send_keys(self.LASTNAME, lastname)

    def enter_mobile(self, mobile):
        self.send_keys(self.MOBILE, mobile)

    def enter_email(self, email):
        self.send_keys(self.EMAIL, email)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    def enter_cpassword(self, cpassword):
        self.send_keys(self.CPASSWORD, cpassword)


    def click_submit(self):
        # Locate the submit button and scroll to it
        submit = self.driver.find_element(*self.SUBMIT)
        self.driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

    def check_submission_status(self):
        try:
            # Try to locate the success element
            success_message = self.driver.find_element(*self.SUCCESS_TOASTER)
            print("Success:", success_message.text)

            # Assert that the success message is displayed
            assert success_message.is_displayed(), "Success message should be displayed."

        except NoSuchElementException:
            # Sequentially check each error element until one is found
            for error_locator in [self.ERROR_1, self.ERROR_2, self.ERROR_3,
                                  self.ERROR_4, self.ERROR_5]:
                try:
                    error_message = self.driver.find_element(*error_locator)
                    print("Error:", error_message.text)

                    # Assert that the error message is displayed
                    assert error_message.is_displayed(), "Error message should be displayed."
                    break  # Exit after finding the first available error message

                except NoSuchElementException:
                    continue  # Move to the next error locator if not found
            else:
                # If no success or error messages are found, assert failure
                assert False, "No success or error messages found."


