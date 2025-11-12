from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome browser
driver = webdriver.Chrome()

# Go to login page
driver.get("https://example.com/login")

# Fill in username and password fields
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("your_username")
password.send_keys("your_password")

# Submit the form
password.send_keys(Keys.RETURN)

# Wait for page to load
time.sleep(3)

print("✅ Login automation completed successfully!")

# Close browser
driver.quit()
