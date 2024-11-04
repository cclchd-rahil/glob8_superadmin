import pytest
from pages.support_ticket_page import SupportTickets

@pytest.mark.usefixtures("login")
def test_faqs(driver):
    support_ticket_page = SupportTickets(driver)
    support_ticket_page.click_support()
    captured_text = support_ticket_page.get_support_title()
    expected_text = "Support Tickets"

    assert captured_text == expected_text, f"Expected '{expected_text}', but got '{captured_text}'"