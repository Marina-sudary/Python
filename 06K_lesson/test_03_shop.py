import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_complete_shopping_flow():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 30)
    try:
        driver.get("https://www.saucedemo.com/")

        username_field = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        add_buttons_ids = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie",
        ]
        for btn_id in add_buttons_ids:
            btn = wait.until(EC.element_to_be_clickable((By.ID, btn_id)))
            btn.click()

        cart_icon = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#shopping_cart_container .shopping_cart_link")
            )
        )
        cart_icon.click()

        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        first_name.send_keys("Марина")
        last_name = driver.find_element(By.ID, "last-name")
        last_name.send_keys("Черныш")
        postal_code = driver.find_element(By.ID, "postal-code")
        postal_code.send_keys("346000")

        continue_btn = driver.find_element(By.ID, "continue")
        continue_btn.click()

        total_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
        )
        total_text = total_element.text
        print("Итоговая сумма:", total_text)

        assert "$58.29" in total_text, f"Стоимость не совпадает, найдено: {total_text}"

    finally:
        driver.quit()
