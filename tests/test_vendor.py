import time
import pytest
from pages.vendor_page import Vendor


@pytest.mark.usefixtures("login")
def test_vendor(driver):
    vendor_page = Vendor(driver)
    vendor_page.click_vendor()
    time.sleep(5)
    vendor_page.click_addnew()
    vendor_page.enter_orgname("Chaincode")
    vendor_page.enter_pan("EPLPR2941F")
    vendor_page.enter_description(" Hello akshat")
    vendor_page.enter_gstin("DVNDVKDFKVMFMV8")
    vendor_page.enter_address("Berlin oak, canada")
    # vendor_page.upload_logo("")
    vendor_page.click_next()
    vendor_page.enter_holdername("Kartik")
    vendor_page.enter_accountnumber("64145656405")
    vendor_page.enter_bankname("State Bank of India")
    vendor_page.enter_branchname("Koppal")
    vendor_page.enter_ifsccode("SBIN0017863")
    vendor_page.click_next()
    vendor_page.enter_firstname("suit")
    vendor_page.enter_lastname("brook")
    vendor_page.enter_mobile("9535005613")
    vendor_page.enter_email("admin3@gmail.com")
    vendor_page.enter_password("Admin@123")
    vendor_page.enter_cpassword("Admin@123")
    vendor_page.click_submit()
    time.sleep(2)
    vendor_page.check_submission_status()
