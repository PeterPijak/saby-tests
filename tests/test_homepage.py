# tests/test_homepage.py

from pages.homepage import HomePage
from main import BASE_URL

def test_saby_homepage(driver):
    page = HomePage(driver)
    page.open(BASE_URL)
    assert "Saby" in driver.title

