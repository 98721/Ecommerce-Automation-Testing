from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def take_screenshot(driver, name="screenshot"):
    if not os.path.exists("reports/screenshots"):
        os.makedirs("reports/screenshots")
    file_path = f"reports/screenshots/{name}.png"
    driver.save_screenshot(file_path)
    return file_path

def test_empty_field_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Empty username & password
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    error_element = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    error_message = error_element.text
    take_screenshot(driver, "empty_login")

    assert "required" in error_message.lower(), f"❌ Empty Field Test Failed: {error_message}"
    print("✅ Empty Field Test Passed")

    driver.quit()

if __name__ == "__main__":
    test_empty_field_login()
