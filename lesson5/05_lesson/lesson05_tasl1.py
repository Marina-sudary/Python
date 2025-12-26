from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")


wait = WebDriverWait(driver, 5)
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-primary')))

button.click()
print("Клик выполнен.")

time.sleep(3)
driver.quit()