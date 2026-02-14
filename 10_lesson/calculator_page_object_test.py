# test_calculator.py
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class Page:
    """
    Базовый класс Page Object.

    Атрибуты:
        driver (WebDriver): активный экземпляр браузера.
        wait (WebDriverWait): объект ожиданий для поиска элементов.

    Методы:
        open() -> None: открыть нужную страницу (реализация в подклассах).
        get_title() -> str: вернуть заголовок текущей страницы.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация базовой страницы.

        Parameters:
            driver (WebDriver): активный экземпляр WebDriver.
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 60)

    def open(self) -> None:
        """Открыть страницу. Реализуется в подклассах."""
        raise NotImplementedError("Subclasses must implement open()")

    def get_title(self) -> str:
        """Вернуть заголовок текущей страницы.

        Returns:
            str: заголовок страницы.
        """
        return self.driver.title


class CalculatorPage(Page):
    """
    Страница "Slow Calculator" с реализацией действий.

    Методы:
        open() -> None
        set_delay(delay_value: int) -> None
        click_button(button_text: str) -> None
        get_result() -> str
        wait_for_result(expected_result: str, timeout: int = 60) -> None
    """

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    @allure.step("Open slow calculator page")
    def open(self) -> None:
        """Открыть страницу калькулятора."""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Set delay to {delay_value}")
    def set_delay(self, delay_value: int) -> None:
        """Установить задержку ввода.

        Parameters:
            delay_value (int): значение задержки, которое нужно ввести в поле задержки.

        Returns:
            None
        """
        delay_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(delay_value))
        self.wait.until(lambda d: delay_input.get_attribute("value") == str(delay_value))

    @allure.step("Click button '{button_text}'")
    def click_button(self, button_text: str) -> None:
        """Нажать кнопку на калькуляторе по тексту кнопки.

        Parameters:
            button_text (str): текст кнопки (например, "7", "+", "=")

        Returns:
            None
        """
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button_text}']"))
        )
        button.click()

    @allure.step("Get result from screen")
    def get_result(self) -> str:
        """Получить текущий результат с экрана калькулятора.

        Returns:
            str: текст результата, например "15"
        """
        result_element = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.screen"))
        )
        return result_element.text

    @allure.step("Wait for result '{expected_result}'")
    def wait_for_result(self, expected_result: str, timeout: int = 60) -> None:
        """Ожидать появления нужного результата на дисплее.

        Parameters:
            expected_result (str): ожидаемое текстовое значение на экране.
            timeout (int): максимальное время ожидания (секунды).

        Returns:
            None
        """
        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), expected_result)
        )


@pytest.fixture
def driver():
    # Можно заменить на Chrome, Firefox и т.д.
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@allure.title("End-to-end: Slow Calculator with Page Object")
@allure.description("Тест проверяет работу slow-calculator через паттерн Page Object и Allure.")
@allure.feature("Page Object Calculator")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(driver: WebDriver) -> None:
    """
    Тест: открой страницу, установи задержку, пройдiй по кнопкам, дождись и проверь результат.
    """
    calculator_page = CalculatorPage(driver)

    with allure.step("Open calculator page"):
        calculator_page.open()

    with allure.step("Set delay to 45"):
        calculator_page.set_delay(45)

    buttons_to_click = ["7", "+", "8", "="]
    with allure.step("Click calculator buttons"):
        for button_text in buttons_to_click:
            calculator_page.click_button(button_text)

    with allure.step("Wait for expected result and verify"):
        calculator_page.wait_for_result("15")
        result = calculator_page.get_result()
        with allure.step(f"Check result equals '15' (actual: {result})"):
            assert result == "15", f"Ожидали '15', получено '{result}'"


if __name__ == "__main__":
    pytest.main([__file__])