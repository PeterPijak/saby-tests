# pages/homepage.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_field = (By.NAME, "q")  # если найдется

    def open(self, url):
        self.driver.get(url)

    def search(self, text):
        search_box = self.driver.find_element(*self.search_field)
        search_box.send_keys(text)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
