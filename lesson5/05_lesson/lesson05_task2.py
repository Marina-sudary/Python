from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
time.sleep(3)


driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
print("Клик выполнен.")

time.sleep(3)

driver.quit()