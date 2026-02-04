import sys
import os
sys.path.append(os.path.dirname(__file__))

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LoginPage import LoginPage
from ProductsPage import ProductsPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage

def test_complete_shopping_flow():
    driver = webdriver.Firefox()
    
    try:
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        products_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]
        
        for product_id in products_to_add:
            products_page.add_product_to_cart(product_id)
        
        products_page.go_to_cart()
        cart_page.checkout()
        
        checkout_page.fill_shipping_info("Марина", "Черныш", "346000")
        checkout_page.continue_checkout()
        
        total_text = checkout_page.get_total_amount()
        print("Итоговая сумма:", total_text)
        
        assert "$58.29" in total_text, f"Стоимость не совпадает, найдено: {total_text}"        
    finally:
        
        driver.quit()

if __name__ == "__main__":
    pytest.main([__file__])