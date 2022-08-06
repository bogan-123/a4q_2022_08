import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver

from HomePage import HomePage
from ProductCategoryPage import ProductCategoryPage
from ProductPage import ProductPage






def test_carrefour():

    # Open browser and go to Web page
    driver = webdriver.Chrome()
    action = ActionChains(driver)
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")

    # Definition of explicit wait
    wait = WebDriverWait(driver, 10)

    # Close cookies pop up
    close_cookies = wait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    close_cookies.click()

def test_page_object():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")

    home = HomePage(driver)
    home.closeCookie()
    home.OpenMenu()
    home.OpenEpicerieSalee()
    home.Open_Sub_category()
    home.Open_Product_category()

    Produit = ProductCategoryPage(driver)
    Produit.OpenProductPage(3)

    Acheter = ProductPage(driver)
    Acheter.Buy()
    Acheter.Choose_Delivery_Method()
    Acheter.Enter_Zip_Code()
    Acheter.Select_First_Store()

    Message_attendu = "1 produit indisponible dans ce magasin."
    assert Acheter.Get_Availability_Status() == Message_attendu









def test_open_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.fr")
    barre_recherche = driver.find_element(By.CSS_SELECTOR,"['#twotabsearchtextbox'")
    time.sleep(2)
    barre_recherche.send_keys("Playsattion 5" + Keys.ENTER)
    driver.quit()




