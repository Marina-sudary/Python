from typing import Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import Page

class CheckoutPage(Page):
    """
    Страница оформления заказа.

    Методы:
        fill_shipping_info(first_name: str, last_name: str, postal_code: str) -> None
        continue_checkout() -> None
        get_total_amount() -> str
    """

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def fill_shipping_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполнить поля доставки.

        Parameters:
            first_name (str): имя
            last_name (str): фамилия
            postal_code (str): почтовый код

        Returns:
            None
        """
        first_name_field = self.wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        first_name_field.send_keys(first_name)

        last_name_field = self.wait.until(EC.visibility_of_element_located((By.ID, "last-name")))
        last_name_field.send_keys(last_name)

        postal_code_field = self.wait.until(EC.visibility_of_element_located((By.ID, "postal-code")))
        postal_code_field.send_keys(postal_code)

    def continue_checkout(self) -> None:
        """Нажать кнопку продолжения оформления заказа."""
        continue_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "continue")))
        continue_btn.click()

    def get_total_amount(self) -> str:
        """Получить текст итоговой суммы на странице заказа.

        Returns:
            str: текст суммы, например "$58.29"
        """
        total_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
        return total_element.text