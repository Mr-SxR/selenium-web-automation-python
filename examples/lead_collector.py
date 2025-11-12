from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Initialize browser
driver = webdriver.Chrome()
driver.get("https://example.com/contacts")

time.sleep(3)

# Create CSV file
with open("leads.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Email"])

    contacts = driver.find_elements(By.CLASS_NAME, "contact-card")

    for contact in contacts:
        name = contact.find_element(By.CLASS_NAME, "contact-name").text
        email = contact.find_element(By.CLASS_NAME, "contact-email").text
        writer.writerow([name, email])

print("✅ Leads collected and saved to leads.csv")

driver.quit()
