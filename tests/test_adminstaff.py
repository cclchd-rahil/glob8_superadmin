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
    adminstaff_page.enter_email("md.rahil+78@chaincodeconsulting.com")
    adminstaff_page.enter_mobilenumber("9535668956")
    index_to_select = 1
    adminstaff_page.select_role_by_index(index_to_select)
    adminstaff_page.enter_password("Admin@123")
    adminstaff_page.enter_cpassword("Admin@123")
    adminstaff_page.click_submit()

    success_messages = adminstaff_page.get_toaster_messages()

    if success_messages['require'] is not None:
        assert success_messages['require'] == "User created successfully!", (
            f"Expected success message: 'User created successfully!', "
            f"but got: '{success_messages['require']}'"
        )
    elif success_messages['error'] is not None:
        assert success_messages['error'] == "Email or mobile already exists", (
            f"Expected error message: 'Email or mobile already exists', "
            f"but got: '{success_messages['error']}'"
        )
    else:
        assert False, "No success or error message found."

