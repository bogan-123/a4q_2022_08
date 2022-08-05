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





def test_css_correction():
    driver = webdriver.Chrome()
    #driver.implicitly_wait(10) #fonctionne avec find_element et find_elements
    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")
    wait = WebDriverWait(driver, 10)
    popup_cookies = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    #time.sleep(2)
    popup_cookies = driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
    popup_cookies.click()
    barre_recherche = driver.find_element(By.CSS_SELECTOR, "input[required]")
    barre_recherche.send_keys("1664" + Keys.ENTER)
    bouton_recherche = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    bouton_recherche.click()
    first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    first_result.click()
    buy_button = driver.find_element(By.CSS_SELECTOR, ".pdp-button-container")
    buy_button.click()
   #time.sleep(2)
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



    from selenium.webdriver.support.select import Select
    # menu dropdown
    select_category = Select(driver.find_element_by_id('searchDropdownBox'))
    select_category.select_by_visible_text()