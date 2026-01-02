from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    wait = WebDriverWait(driver, 10)
    input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="number"]')))

    input_field.send_keys("Sky")
    time.sleep(3)
    
    input_field.clear()
    time.sleep(3)
    
    input_field.send_keys("Pro")
    time.sleep(3)

finally:
    driver.quit()
