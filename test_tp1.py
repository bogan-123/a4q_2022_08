import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_open_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.fr")
    barre_recherche = driver.find_element(By.XPATH, "[//input[@id='twotabsearchtextbox']")
    time.sleep(2)
    barre_recherche.send_keys("Playsattion 5" + Keys.ENTER)
    driver.quit()



