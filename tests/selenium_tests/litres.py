import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://www.litres.ru/')
driver.maximize_window()
driver.implicitly_wait(10)

def test_button():
    found_button = driver.find_element(By.CLASS_NAME, "_8fba8811")
    found_button.click()
    element = driver.find_element(By.CLASS_NAME, "_8fba8811")
    element.send_keys("Пушкин")
    found_button = driver.find_element(By.CLASS_NAME, "_82b1c248")
    found_button.click()
    element = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.CLASS_NAME, "d27c46ab"))
    )
    text_elements= driver.find_elements(By.CSS_SELECTOR, "[data-testid = 'art__title']")
    pass

