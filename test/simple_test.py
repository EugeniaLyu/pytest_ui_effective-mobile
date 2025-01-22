import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from page.MainPage import MainPage


def test_first():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(4)
    browser.maximize_window()

    main_page = MainPage(browser)
    main_page.go()

    time.sleep(5)
