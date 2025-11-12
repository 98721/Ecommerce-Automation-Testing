from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import os

def load_invalid_credentials():
    with open("data/credentials.json") as f:
        return json.load(f)["invalid_user"]

def take_screenshot(driver, name="screenshot"):
    if not os.path.exists("reports/screenshots"):
        os.makedirs("reports/screenshots")
    file_path = f"reports/screenshots/{name}.png"
    driver.save_screenshot(file_path)
    return file_path

def test_invalid_login():
    creds = load_invalid_credentials()
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys(creds["username"])
    driver.find_element(By.ID, "password").send_keys(creds["password"])
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    error_element = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    error_message = error_element.text
    take_screenshot(driver, "invalid_login")

    assert "invalid" in error_message.lower(), f"❌ Invalid Login Test Failed: {error_message}"
    print("✅ Invalid Login Test Passed")

    driver.quit()

if __name__ == "__main__":
    test_invalid_login()
