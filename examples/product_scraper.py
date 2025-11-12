from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize browser
driver = webdriver.Chrome()

# Target URL
driver.get("https://example.com/products")

time.sleep(2)  # wait for products to load

# Find product elements
products = driver.find_elements(By.CLASS_NAME, "product-card")

for product in products:
    title = product.find_element(By.CLASS_NAME, "product-title").text
    price = product.find_element(By.CLASS_NAME, "product-price").text
    print(f"{title} — {price}")

print("✅ Product data extracted successfully!")

driver.quit()
