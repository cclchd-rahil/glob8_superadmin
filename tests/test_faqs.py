import time

import pytest
from pages.faqs_page import Faqs

@pytest.mark.usefixtures("login")
def test_faqs(driver):
    faqs_page = Faqs(driver)
    faqs_page.click_faqs()
    captured_text = faqs_page.get_faqs_title()
    expected_text = "FAQs"

    assert captured_text == expected_text, f"Expected '{expected_text}', but got '{captured_text}'"