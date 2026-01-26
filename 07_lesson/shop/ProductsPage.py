import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
    
    def add_product_to_cart(self, product_id):
        btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, product_id))
        )
        btn.click()
    
    def go_to_cart(self):
        cart_icon = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#shopping_cart_container .shopping_cart_link")
            )
        )
        cart_icon.click()