# Automation Testing Suite for Admin Portal

This project contains automated tests for the login functionality of the Admin portal, built with Python, Selenium, and Pytest.

# Project Structure

    glob8_superadmin/
    ├── pages/                # Page Object Model files
    ├── tests/                # Test cases
    ├── utils/                # Utility functions
    └── .venv/                # Virtual environment


# Pre-requisites

Ensure you have the following installed:
 * Python 3.x
 * Selenium 
 * Pytest for running test cases

# How to Run Tests

  1. Activate the Virtual Environment:

          # On Windows
          .venv\Scripts\activate
          # On MacOS/Linux
          source .venv/bin/activate

  2. Run Tests:

         pytest tests/test_login.py --headless
                            or
         pytest

# CI/CD Integration

  1. Install Dependencies:

           pip install -r requirements.txt

  2. Run Tests in Headless Mode:

           pytest tests/test_login.py --headless --junitxml=report.xml

  3. Collect Test Reports:

      * Configure your CI/CD tool to read report.xml for test results.

# Test Cases

**The test suite includes 5 cases covering the login functionality of the Admin portal. The tests are designed to verify:**

1. Successful login with valid credentials
2. Login failure with invalid credentials
3. Validation of missing input fields (email)
4. Validation of missing input fields (password)
5. Validation of missing input fields (email and password)
