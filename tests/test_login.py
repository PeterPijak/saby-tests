import pytest
from pages.login_page import HomePage
from main import BASE_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(driver):
    login_page = HomePage(driver)

    # Открываем сайт
    login_page.open()

    # Переходим на страницу авторизации
    login_page.click_start_button()

    # Вводим логин и пароль
    login_page.enter_login("testqa")
    login_page.enter_password("testqa!1")

    # Переключаемся на iframe с reCAPTCHA, если он есть
    try:
        WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "a-rnkgaatv21e")))
        print("Переключился на reCAPTCHA iframe")
    except Exception as e:
        print("Не удалось переключиться на reCAPTCHA iframe:", e)

    driver.switch_to.default_content()  # Возвращаемся в основной контент страницы

    # Нажимаем на кнопку "Войти"
    login_page.submit_login()


