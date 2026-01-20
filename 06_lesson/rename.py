from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By #

from selenium.webdriver.support.ui import WebDriverWait #
from selenium.webdriver.support import expected_conditions as EC # 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#newButtonName"))
    )
input_text = "SkyPro"
input_field.clear()
input_field.send_keys(input_text)
    

update_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#updatingButton"))
    )
update_button.click()
    
button_text = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#updatingButton"))
    ).text
    
print(button_text)
    
driver.quit()