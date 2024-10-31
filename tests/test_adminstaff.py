import pytest
from pages.adminstaff_page import Admin
from selenium.webdriver.common.by import By
from pages import login_page
from pages.login_page import LoginPage


@pytest.mark.usefixtures("login")
def test_add(driver):
    adminstaff_page = Admin(driver)
    adminstaff_page.click_admin()
    adminstaff_page.click_addnew()
    adminstaff_page.enter_firstname("Rahil")
    adminstaff_page.enter_lastname("Rahil")
    adminstaff_page.enter_email("md.rahil@chaincodeconsulting.com")
