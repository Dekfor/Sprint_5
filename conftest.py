import pytest
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture
def email():
    return f"test{random.randint(10000,99999)}@mail.com"

def wait_element(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )