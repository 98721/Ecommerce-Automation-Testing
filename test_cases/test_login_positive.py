from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import os

def load_credentials():
    with open("data/credentials.json") as f:
        return json.load(f)["valid_user"]

def take_screenshot(driver, name="screenshot"):
    if not os.path.exists("reports/screenshots"):
        os.makedirs("reports/screenshots")
    file_path = f"reports/screenshots/{name}.png"
    driver.save_screenshot(file_path)
    return file_path

def test_valid_login():
    creds = load_credentials()
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys(creds["username"])
    driver.find_element(By.ID, "password").send_keys(creds["password"])
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    take_screenshot(driver, "valid_login")
    assert "inventory" in driver.current_url, "Login failed!"
    print("✅ Valid Login Test Passed")

    driver.quit()

if __name__ == "__main__":
    test_valid_login()
