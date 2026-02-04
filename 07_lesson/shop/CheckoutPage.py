import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
    
    def fill_shipping_info(self, first_name, last_name, postal_code):
        first_name_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys(first_name)
        
        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys(last_name)
        
        postal_code_field = self.driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys(postal_code)
    
    def continue_checkout(self):
        continue_btn = self.driver.find_element(By.ID, "continue")
        continue_btn.click()
    
    def get_total_amount(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
        )
        return total_element.text