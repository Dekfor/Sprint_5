import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def generate_email():
    return f"test{random.randint(10000,99999)}@mail.com"

def wait_element(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
