import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def test_open_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")
    time.sleep(2)
    popup_cookies = driver.find_element(By.CSS_SELECTOR,".banner-actions-container > button")
    popup_cookies.click()
    barre_recherche = driver.find_element(By.CSS_SELECTOR,"input[required]")
    barre_recherche.send_keys("1664" + Keys.ENTER)
    bouton_recherche = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    bouton_recherche.click()
    first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    first_result.click()
    buy_button = driver.find_element(By.CSS_SELECTOR, ".pdp-button-container")
    buy_button.click()
    time.sleep(2)
    retrait_en_magasin = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")
    delivery24 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(2) label")
    delivery1 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(3) label")
    assert retrait_en_magasin.text == 'Drive\nRetrait gratuit en magasin'
    print('Selector "retrait en drive" is present')
    assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
    print('Selector "livraison en 24h" is present')
    assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
    print('Selector "livraison en 1h" is present')
    # presence des 3 selectors
    # time.sleep(2)
    driver.quit()