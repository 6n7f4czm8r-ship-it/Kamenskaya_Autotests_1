import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://perm.medsi.ru/')
driver.maximize_window()
driver.implicitly_wait(10)

# def test_button():
#     found_button = driver.find_element(By.ID, "navP")
#     found_button.click()
#     text_element = driver.find_element(By.XPATH, "//h1[contains(text(), 'Услуги в г. Пермь')]")
#     text = text_element.text
#     assert text == "Услуги в г. Пермь"
#     driver.quit()

def test_button_1():
    found_button = driver.find_element(By.CLASS_NAME, "btn btn-yellow for-utm-link")
    found_button.click()
    driver.quit()