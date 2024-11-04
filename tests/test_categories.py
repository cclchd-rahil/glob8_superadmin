import pytest
from pages.categories_pages import Categories


@pytest.mark.usefixtures("login")
def test_categories(driver):
    categories_pages = Categories(driver)
    categories_pages.click_categories()
    captured_text = categories_pages.get_categories_title()
    expected_text = "Categories"

    assert captured_text == expected_text, f"Expected '{expected_text}', but got '{captured_text}'"