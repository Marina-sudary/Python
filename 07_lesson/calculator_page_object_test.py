# test_calculator.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
    
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def set_delay(self, delay_value):
        delay_input = self.wait.until(
            EC.element_to_be_clickable(("css selector", "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(delay_value))
        self.wait.until(lambda d: delay_input.get_attribute("value") == str(delay_value))
    
    def click_button(self, button_text):
        button = self.wait.until(
            EC.element_to_be_clickable(("xpath", f"//span[text()='{button_text}']"))
        )
        button.click()
    
    def get_result(self):
        result_element = self.wait.until(
            EC.presence_of_element_located(("css selector", "div.screen"))
        )
        return result_element.text
    
    def wait_for_result(self, expected_result, timeout=60):
        self.wait.until(
            EC.text_to_be_present_in_element(("css selector", "div.screen"), expected_result)
        )


def test_slow_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    try:
        calculator_page = CalculatorPage(driver)
        
        calculator_page.open()
        
        calculator_page.set_delay(45)
        
        buttons_to_click = ["7", "+", "8", "="]
        for button_text in buttons_to_click:
            calculator_page.click_button(button_text)
        
        calculator_page.wait_for_result("15")
        result = calculator_page.get_result()
        
        assert result == "15", f"Ожидали '15', получено '{result}'"
        
    finally:
        driver.quit()


if __name__ == "__main__":
    pytest.main([__file__])