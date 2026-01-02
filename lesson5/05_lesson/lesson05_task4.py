from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

try:
    # Переход на страницу
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(2)

    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")
    time.sleep(2)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")
    time.sleep(2)

    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius[type='submit']")
    login_button.click()
    time.sleep(2)

   
    flash_message_element = driver.find_element(By.ID, "flash")
    flash_text = flash_message_element.text
    print(flash_text)

finally:
    driver.quit()