import time

import wait
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class HomePage:
        #self appartient a la classe homepage et init pour initialiser la class homepage

    close_cookie_button_selector = "onetrust-accept-btn-handler"
    hamburger_button_selector = "#data-rayons"
    epicerie_salee_selector = ".nav-item__menu-link [alt='Epicerie salée']"
    sub_category_selector = "#data-menu-level-1_R12 > li:nth-child(7)"
    category_product_selector = "#data-menu-level-2_R13F05 > li:nth-child(3)"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    # close cookie
    def closeCookie(self):
          closeCookieButton = self.wait.until(expected_conditions.element_to_be_clickable((By.ID, self.close_cookie_button_selector)))
          closeCookieButton.click()
          self.wait.until(expected_conditions.invisibility_of_element_located((By.ID, self.close_cookie_button_selector)))


    #OpenMenuhamburger
    def OpenMenu(self):
        self.driver.find_element(By.CSS_SELECTOR, self.hamburger_button_selector).click()


    # hover to epicerie salee

    def OpenEpicerieSalee(self):
        epicerie_salee = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.epicerie_salee_selector)))
        action = ActionChains(self.driver)
        action.move_to_element(epicerie_salee)
        action.perform()

    #OpenSubCategoryMenu(subcategoryMenu)

    def Open_Sub_category(self):
        sub_categry_feculent = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.sub_category_selector)))
        action = ActionChains(self.driver)
        action.move_to_element(sub_categry_feculent)
        action.perform()

    #OpenProductCategoryPage
    def Open_Product_category(self):
        self.driver.find_element(By.CSS_SELECTOR, self.category_product_selector).click()
        time.sleep(2)









