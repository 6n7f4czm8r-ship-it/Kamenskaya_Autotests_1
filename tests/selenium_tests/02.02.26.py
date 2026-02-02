import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.litres.ru")
driver.maximize_window()
driver.implicitly_wait(10)

def test_get_text():
    found_button = driver.find_element(By.CSS_SELECTOR, "input._8fba8811")
    found_button.click()
    driver.quit()