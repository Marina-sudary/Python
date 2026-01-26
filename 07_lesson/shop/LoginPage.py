import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
    
    def open(self):
        self.driver.get("https://www.saucedemo.com/")
    
    def login(self, username, password):
        username_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys(username)
        
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
