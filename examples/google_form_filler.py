from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://forms.gle/example_form_link")

time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("John Doe")
driver.find_element(By.XPATH, "//textarea").send_keys("This is a test submission.")
driver.find_element(By.XPATH, "//span[text()='Submit']").click()

print("✅ Form submitted successfully!")
driver.quit()
