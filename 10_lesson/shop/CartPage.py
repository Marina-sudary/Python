from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import Page

class CartPage(Page):
    """
    Страница корзины (Cart) в Sauce Demo.

    Методы:
        checkout() -> None: перейти к оформлению заказа.
    """

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def checkout(self) -> None:
        """
        Открыть страницу оформления заказа.

        Returns:
            None
        """
        checkout_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_btn.click()