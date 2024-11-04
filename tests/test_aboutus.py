import pytest
from pages.about_us_page import AboutUs


@pytest.mark.usefixtures("login")
def test_about_us(driver):
    about_us_page = AboutUs(driver)
    about_us_page.click_about_us()
    captured_text = about_us_page.get_tittle_element()
    expected_text = "About NFTtrace"

    assert captured_text == expected_text, f"Expected '{expected_text}', but got '{captured_text}'"