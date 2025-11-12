from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

driver = webdriver.Chrome()
driver.get("https://example-dashboard.com/login")

# Login
driver.find_element(By.ID, "username").send_keys("demo_user")
driver.find_element(By.ID, "password").send_keys("demo_pass")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)

# Go to reports
driver.get("https://example-dashboard.com/reports")
time.sleep(2)

# Click download button
driver.find_element(By.ID, "download-report").click()
time.sleep(5)

print("✅ Report downloaded successfully!")
driver.quit()
