import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_slow_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 60)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        delay_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys("45")

        button_texts = ["7", "+", "8", "="]
        for text in button_texts:
            
            button = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                f"//span[contains(@class, 'btn') and contains(text(), '{text}')]"
            )))
            button.click()

        answer_locator = (By.CSS_SELECTOR, "div.screen")
        
        wait.until(EC.text_to_be_present_in_element(answer_locator, "15"))

      
        result_text = driver.find_element(*answer_locator).text
        assert result_text == "15", f"Ожидали '15', получено '{result_text}'"

    finally:
        driver.quit()

