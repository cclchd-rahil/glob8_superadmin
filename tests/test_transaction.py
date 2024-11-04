import pytest
from pages.transactions_page import Transaction

@pytest.mark.usefixtures("login")
def test_transaction(driver):
    transactions_page =Transaction(driver)
    transactions_page.click_transaction()
    captured_text = transactions_page.get_transaction_title()  # Assuming a method to get text
    expected_text = "Transactions"  # Replace with the expected value

    # Assert that the captured text matches the expected value
    assert captured_text == expected_text, f"Expected '{expected_text}', but got '{captured_text}'"



