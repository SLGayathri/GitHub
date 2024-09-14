from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (assuming using Chrome)
driver = webdriver.Chrome()

# Define the URL of the application to be tested
url = "http://your-application-url.com/login"

# Open the application
driver.get(url)

# Helper function to find elements and wait if needed
def find_element(by, value, wait=10):
    return WebDriverWait(driver, wait).until(
        EC.presence_of_element_located((by, value))
    )

# Test Case 1: Valid username and password
def test_valid_login():
    try:
        driver.get(url)
        find_element(By.NAME, "username").send_keys("valid-username")
        find_element(By.NAME, "password").send_keys("valid-password")
        find_element(By.XPATH, "//button[@type='submit']").click()
        find_element(By.ID, "logged-in-element-id")
        print("Test valid login: Passed")
    except Exception as e:
        print(f"Test valid login: Failed - {e}")

# Test Case 3: Empty username and password
def test_empty_login():
    try:
        driver.get(url)
        find_element(By.XPATH, "//button[@type='submit']").click()
        find_element(By.ID, "empty-fields-error-message")
        print("Test empty login: Passed")
    except Exception as e:
        print(f"Test empty login: Failed - {e}")

# Test Case 4: Valid username and invalid password
def test_valid_username_invalid_password():
    try:
        driver.get(url)
        find_element(By.NAME, "username").send_keys("valid-username")
        find_element(By.NAME, "password").send_keys("invalid-password")
        find_element(By.XPATH, "//button[@type='submit']").click()
        find_element(By.ID, "login-error-message")
        print("Test valid username and invalid password: Passed")
    except Exception as e:
        print(f"Test valid username and invalid password: Failed - {e}")

# Test Case 5: Invalid username and valid password
def test_invalid_username_valid_password():
    try:
        driver.get(url)
        find_element(By.NAME, "username").send_keys("invalid-username")
        find_element(By.NAME, "password").send_keys("valid-password")
        find_element(By.XPATH, "//button[@type='submit']").click()
        find_element(By.ID, "login-error-message")
        print("Test invalid username and valid password: Passed")
    except Exception as e:
        print(f"Test invalid username and valid password: Failed - {e}")

# Test Case 6: Logging in with existing username
def test_existing_username_login():
    try:
        driver.get(url)
        find_element(By.NAME, "username").send_keys("existing-username")
        find_element(By.NAME, "password").send_keys("existing-password")
        find_element(By.XPATH, "//button[@type='submit']").click()
        find_element(By.ID, "logged-in-element-id")
        print("Test existing username login: Passed")
    except Exception as e:
        print(f"Test existing username login: Failed - {e}")

# Test Case 7: Forgot password
def test_forgot_password():
    try:
        driver.get(url)
        find_element(By.LINK_TEXT, "Forgot Password?").click()
        find_element(By.NAME, "email").send_keys("valid-email@example.com")
        find_element(By.XPATH, "//button[@type='submit']").click()
        find_element(By.ID, "reset-password-confirmation")
        print("Test forgot password: Passed")
    except Exception as e:
        print(f"Test forgot password: Failed - {e}")

# Test Case 8: Sign up option
def test_sign_up():
    try:
        driver.get(url)
        find_element(By.LINK_TEXT, "Sign Up").click()
        find_element(By.NAME, "username").send_keys("new-username")
        find_element(By.NAME, "email").send_keys("new-email@example.com")
        find_element(By.NAME, "password").send_keys("new-password")
        find_element(By.XPATH, "//button[@type='submit']").click()
        find_element(By.ID, "signup-confirmation")
        print("Test sign up: Passed")
    except Exception as e:
        print(f"Test sign up: Failed - {e}")

# Test Case 9: Sign in using Gmail
def test_sign_in_gmail():
    try:
        driver.get(url)
        find_element(By.XPATH, "//button[@id='google-sign-in']").click()
        # Add logic for Google sign-in if required
        print("Test sign in using Gmail: Passed")
    except Exception as e:
        print(f"Test sign in using Gmail: Failed - {e}")

# Test Case 10: Sign in using Facebook
def test_sign_in_facebook():
    try:
        driver.get(url)
        find_element(By.XPATH, "//button[@id='facebook-sign-in']").click()
        # Add logic for Facebook sign-in if required
        print("Test sign in using Facebook: Passed")
    except Exception as e:
        print(f"Test sign in using Facebook: Failed - {e}")

# Test Case 11: Sign in using LinkedIn
def test_sign_in_linkedin():
    try:
        driver.get(url)
        find_element(By.XPATH, "//button[@id='linkedin-sign-in']").click()
        # Add logic for LinkedIn sign-in if required
        print("Test sign in using LinkedIn: Passed")
    except Exception as e:
        print(f"Test sign in using LinkedIn: Failed - {e}")

# Test Case 12: Password masked
def test_password_masked():
    try:
        driver.get(url)
        password_field = find_element(By.NAME, "password")
        if password_field.get_attribute("type") == "password":
            print("Test password masked: Passed")
        else:
            print("Test password masked: Failed")
    except Exception as e:
        print(f"Test password masked: Failed - {e}")

# Running all test cases
test_valid_login()
test_invalid_login()
test_empty_login()
test_valid_username_invalid_password()
test_invalid_username_valid_password()
test_existing_username_login()
test_forgot_password()
test_sign_up()
test_sign_in_gmail()
test_sign_in_facebook()
test_sign_in_linkedin()
test_password_masked()

# Close the browser
driver.quit()
