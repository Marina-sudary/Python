import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.common.exceptions import TimeoutException

def get_border_color(element):
    return element.value_of_css_property('border-color')

@pytest.fixture
def driver():
    service = Service(r"C:\Users\User\Downloads\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_zip_code_validation(driver):
    wait = WebDriverWait(driver, 25)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for name, value in form_data.items():
        field = wait.until(EC.presence_of_element_located((By.NAME, name)))
        field.clear()
        field.send_keys(value)

    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    try:
        zip_div = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    except TimeoutException:
        print("Элемент #zip-code не найден или не появится в течение времени ожидания.")
        raise

    zip_class = zip_div.get_attribute("class")
    print(f"Класс у #zip-code: {zip_class}")

    if "alert-danger" in zip_class:
        print("ZIP-код подсвечен красным (ожидаемое поведение).")
    else:
        print("Значение класса у #zip-code не содержит alert-danger — тест не прошел.")
        raise AssertionError("ZIP-код не подсвечен alert-danger.")

    fields_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field_id in fields_to_check:
        try:
            elem = wait.until(EC.presence_of_element_located((By.ID, field_id)))
            classes = elem.get_attribute("class")
            print(f"{field_id} class: {classes}")
            
            assert "alert-success" in classes, f"{field_id} не подсвечено green (alert-success)"
        except TimeoutException:
            print(f"Элемент с ID='{field_id}' не найден.")
            raise
        except AssertionError as e:
            print(str(e))
            raise

        finally:
            driver.quit()
 