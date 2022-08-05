from datetime import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_open_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")
    Popup_cookies = driver.find_element(By.XPATH, "['//button[@id=onetrust-accept-btn-handler']")
    Popup_cookies.click()
    time.sleep(2)
    #barre_recherche = driver.find_element(By.XPATH,['//input[@aria-label=Rechercher parmi le contenu du site'])
    #barre_recherche.send_keys("1664" + Keys.ENTER)
    ##driver.quit()
