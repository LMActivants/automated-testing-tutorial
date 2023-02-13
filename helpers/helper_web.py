from selenium import webdriver
from helpers.helper_base import HelperFunc

def get_browser(browser):
    path = 'C:\chromedriver.exe'
    if browser == "chrome":
        return HelperFunc(webdriver.Chrome(path))