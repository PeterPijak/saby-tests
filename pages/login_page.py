from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    START_BUTTON = (By.CSS_SELECTOR, 'span.sbisru-Button__caption')
    LOGIN_FIELD = (By.XPATH, '//input[@placeholder="﻿" and @name="ws-input_2025-08-30"]')  # Используем placeholder
    PASSWORD_FIELD = (By.NAME, 'ws-input_2025-08-30')
    LOGIN_BUTTON = (By.XPATH, '//span[contains(@class, "auth-AdaptiveLoginForm__loginButtonImage")]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Ожидаем 10 секунд

    def open(self):
        self.driver.get("https://saby.ru/")

    def click_start_button(self):
        self.wait.until(EC.element_to_be_clickable(self.START_BUTTON)).click()

    def enter_login(self, login):
        login_field = self.wait.until(EC.visibility_of_element_located(self.LOGIN_FIELD))
        login_field.send_keys(login)

    def enter_password(self, password):
        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        password_field.send_keys(password)

    def submit_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
