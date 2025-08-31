# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from main import CHROMEDRIVER_PATH
import os

@pytest.fixture
def driver():
    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed and "driver" in item.fixturenames:
        driver = item.funcargs["driver"]
        screenshot_dir = "./screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_file = os.path.join(screenshot_dir, f"{item.name}.png")
        driver.save_screenshot(screenshot_file)
