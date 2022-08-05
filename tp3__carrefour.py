import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def test_tp3_carrefour():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get("https://www.carrefour.fr/"

    #definition of explicit wait
    wait = WebDriverWait(driver, 10)

    #close cookies
    close_cookies_button = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    close_cookies_button.click()
    #hover on
    hamburger_button = driver.find_element(By.CSS_SELECTOR, ".mainbar__nav-toggle-icon")
    hamburger_button.click()

    epicerie_salee_menu = driver.find_element(By.CSS_SELECTOR, ".nav-item__menu-link [alt='Epicerie salée']")
    action = ActionChains(driver)
    action.move_to_element(epicerie_salee_menu)
    action.perform()

    time.sleep(3)
    pates_riz_sous_menu = driver.find_element(By.CSS_SELECTOR, "#data-menu-level-1_R12 > li:nth-child(7)")
    action = ActionChains(driver)
    action.move_to_element(pates_riz_sous_menu)
    action.perform()
    time.sleep(3)
    cliquer_choisir_pates = driver.find_element(By.CSS_SELECTOR, "#data-menu-level-2_R12F05 > li:nth-child(3)")
    cliquer_choisir_pates.click()

    #Open 4th product
    def openProduct(driver, index):
        liste_produits = driver.find_elements(By.CSS_SELECTOR, ".product-grid-item:not([data-format])  h2")
        liste_produits[3].click()
        openProduct(driver, 3)

    #Acheter le produit
    buy_button = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".pdp-button-container")))
    buy_button.click()
    driver.quit()
