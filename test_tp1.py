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
    