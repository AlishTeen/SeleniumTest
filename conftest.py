from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://demoqa.com/automation-practice-form")
    yield browser
    browser.quit()
