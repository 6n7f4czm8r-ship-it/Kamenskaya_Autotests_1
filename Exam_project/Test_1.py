#1 закрытие всплывающего окна
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://perm.medsi.ru/')
driver.maximize_window()
driver.implicitly_wait(10)

def test_button_1():
    try:
        close_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cookie-alert__button js-save-cookie-btn"))
        )
        close_button.click()
        print("Всплывающее окно закрыто")
    except:
        print("Окно не появилось")

# def test_button_2():
#     found_button = driver.find_element(By.XPATH, "//a[text()='Записаться на прием']")
#     found_button.click()
#     assert text == "Записаться на прием"
#     driver.quit()
