import os
import sys
sys.path.append(os.path.dirname(__file__))

import pytest
import allure
from selenium import webdriver

from shop.LoginPage import LoginPage
from shop.ProductsPage import ProductsPage
from shop.CartPage import CartPage
from shop.CheckoutPage import CheckoutPage

@allure.title("Complete shopping flow with Page Object")
@allure.description("End-to-end тест: логин → выбор товара → корзина → оформление заказа.")
@allure.feature("Sauce Demo - Page Object")
@allure.severity(allure.severity_level.CRITICAL)
def test_complete_shopping_flow(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открыть страницу входа и залогиниться"):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    products_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]

    with allure.step("Добавить товары в корзину"):
        for product_id in products_to_add:
            products_page.add_product_to_cart(product_id)

    with allure.step("Перейти в корзину и начать оформление"):
        products_page.go_to_cart()
        cart_page.checkout()

    with allure.step("Заполнить данные доставки и продолжить оформление"):
        checkout_page.fill_shipping_info("Марина", "Черныш", "346000")
        checkout_page.continue_checkout()

    with allure.step("Получить итоговую сумму и проверить"):
        total_text = checkout_page.get_total_amount()
        print("Итоговая сумма:", total_text)

        with allure.step("Проверить ожидаемую сумму"):
            assert "$58.29" in total_text, f"Стоимость не совпадает, найдено: {total_text}"

# фикстура драйвера
@pytest.fixture
def driver():
    # Меняем браузер здесь при необходимости: Firefox, Chrome, etc.
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

if __name__ == "__main__":
    pytest.main([__file__])