from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import Page

class ProductsPage(Page):
    """
    Страница товаров.

    Методы:
        add_product_to_cart(product_id: str) -> None
        go_to_cart() -> None
    """

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def add_product_to_cart(self, product_id: str) -> None:
        """Добавить товар в корзину.

        Parameters:
            product_id (str): ID кнопки добавления в корзину
        Returns:
            None
        """
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, product_id)))
        btn.click()

    def go_to_cart(self) -> None:
        """Перейти в корзину.

        Returns:
            None
        """
        cart_icon = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#shopping_cart_container .shopping_cart_link")))
        cart_icon.click()