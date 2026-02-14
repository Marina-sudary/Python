import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import Page

class LoginPage(Page):
    """
    Страница логина.

    Методы:
        open() -> None
        login(username: str, password: str) -> None
    """

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def open(self) -> None:
        """Открыть страницу входа."""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """
        Выполнить вход.

        Parameters:
            username (str): имя пользователя
            password (str): пароль

        Returns:
            None
        """
        username_field = self.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys(username)

        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.send_keys(password)

        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
