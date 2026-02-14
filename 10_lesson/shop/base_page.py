from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

class Page:
    """
    Базовый класс Page Object.

    Аттрибуты:
        driver (WebDriver): активный драйвер браузера.
        wait (WebDriverWait): явные ожидания для поиска элементов.

    Методы (для наследников):
        open() -> None: открыть нужную страницу.
        get_title() -> str: вернуть заголовок страницы.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация базовой страницы.

        Parameters:
            driver (WebDriver): активный экземпляр WebDriver.
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 30)

    def open(self) -> None:
        """Открыть страницу. Реализуется в подклассах."""
        raise NotImplementedError("Subclasses must implement open()")

    def get_title(self) -> str:
        """Вернуть заголовок текущей страницы.

        Returns:
            str: заголовок страницы.
        """
        return self.driver.title