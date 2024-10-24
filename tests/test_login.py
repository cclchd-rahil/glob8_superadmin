from selenium.webdriver.common.by import By
from pages import login_page
from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page =LoginPage(driver)

    driver.get("https://admin.nfttrace.com/login")
    driver.maximize_window()
    login_page.enter_email("superadmin@gmail.com")
    login_page.enter_password("admin@123")
    login_page.click_login()

    expected_title = "NFTtrace Marketplace - Login to Manage and Track Your NFTs with Ease"
    assert driver.title == expected_title, f"Expected title '{expected_title}', but got '{driver.title}'"

def test_invalid_login(driver):
    login_page = LoginPage(driver)

    driver.get("https://admin.nfttrace.com/login")
    driver.maximize_window()
    login_page.enter_email("superdmin@gmail.com")
    login_page.enter_password("admin@123")
    login_page.click_login()

    error_messages = login_page.get_error_messages()

    assert error_messages['require'] == "Something went wrong!", (f"Expected {error_messages}, "
                                                                         f"but got '{error_messages['require']}")

def test_empty_email(driver):
    login_page = LoginPage(driver)

    driver.get("https://admin.nfttrace.com/login")
    driver.maximize_window()
    login_page.enter_email("")
    login_page.enter_password("admin@123")
    login_page.click_login()

    error_messages = login_page.get_error_messages()

    assert error_messages['email'] == "Email is required", (f"Expected {error_messages}, "
                                                                         f"but got '{error_messages}")
def test_empty_password(driver):
    login_page = LoginPage(driver)

    driver.get("https://admin.nfttrace.com/login")
    driver.maximize_window()
    login_page.enter_email("superdmin@gmail.com")
    login_page.enter_password("")
    login_page.click_login()

    error_messages = login_page.get_error_messages()

    assert error_messages['password'] == "Password is required", (f"Expected {error_messages}, "
                                                                         f"but got '{error_messages}")

def test_empty_email_password(driver):
    login_page = LoginPage(driver)

    driver.get("https://admin.nfttrace.com/login")
    driver.maximize_window()
    login_page.enter_email("")
    login_page.enter_password("")
    login_page.click_login()

    error_messages = login_page.get_error_messages()

    assert error_messages[
               'email'] == "Email is required", f"Expected 'Email is required', but got '{error_messages['email']}'"
    assert error_messages[
               'password'] == "Password is required", f"Expected 'Password is required', but got '{error_messages['password']}'"







