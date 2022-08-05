from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def __init__(self, driver: webdriver.Chrome):
    self.driver = driver
    self.wait = WebDriverWait(driver, 10)

class Screenshots:
    def Screenshots(self):
        self.driver.get_screenshot_as_file("C:\Users\ib\Downloads\Screenshots\capture.png")
