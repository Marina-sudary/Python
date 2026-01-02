from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")
wait = WebDriverWait(driver, 25)

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success")))

txt = success_message.text
print(txt)

driver.quit()