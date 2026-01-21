from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 60)

    try:
        # Открываем страницу
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

        # Вводим задержку
        delay_input = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys("45")

        # Добавляем небольшую паузу, чтобы значение применилось
        wait.until(lambda d: delay_input.get_attribute("value") == "45")

        # Клики по кнопкам: 7, +, 8, =
        button_texts = ["7", "+", "8", "="]
        for text in button_texts:
            button = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//span[text()='{text}']"))
            )
            button.click()

        # Проверка результата
        answer_locator = (By.CSS_SELECTOR, "div.screen")
        wait.until(EC.text_to_be_present_in_element(answer_locator, "15"))

        result_text = driver.find_element(*answer_locator).text
        assert result_text == "15", f"Ожидали '15', получено '{result_text}'"

    finally:
        driver.quit()
