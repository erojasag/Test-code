from cgi import test
from tracemalloc import start
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import logging
import config


def start_connection():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(config.website)
    return driver


def test_netflix_login(driver):
    driver.implicitly_wait(0.5)
    driver.find_element_by_link_text('Sign In').click()
    driver.find_element_by_id('id_userLoginId').send_keys(config.username)
    driver.find_element_by_id('id_password').send_keys(config.password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    driver.implicitly_wait(0.5)


def test_netflix_user_selection(driver):
    driver.implicitly_wait(0.5)
    driver.find_element_by_link_text('Sign In').click()
    driver.implicitly_wait(0.5)
    driver.find_element_by_id('id_userLoginId').send_keys(config.username)
    driver.implicitly_wait(0.5)
    driver.find_element_by_id('id_password').send_keys(config.password)
    driver.implicitly_wait(0.5)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    driver.implicitly_wait(0.5)
    driver.find_element_by_link_text(config.profile).click()
    driver.implicitly_wait(0.5)
    test_netflix_logout(driver)
    driver.implicitly_wait(0.5)
    logging.info()

def test_netflix_search(driver):
    driver.implicitly_wait(0.5)
    driver.find_element_by_link_text('Sign In').click()
    driver.find_element_by_id('id_userLoginId').send_keys(config.username)
    driver.find_element_by_id('id_password').send_keys(config.password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    driver.implicitly_wait(0.5)
    driver.find_element_by_link_text(config.profile).click()
    driver.implicitly_wait(0.5)
    driver.find_element_by_xpath('//button[@class="searchTab"]').click()
    driver.implicitly_wait(1.5)
    driver.find_element_by_id("searchInput").send_keys("The Matrix")
    driver.implicitly_wait(1.5)
    driver.find_element_by_xpath('//button[@class="searchButton"]').click()
    driver.implicitly_wait(1.5)

def test_netflix_logout(driver):
    driver.implicitly_wait(0.5)
    driver.find_element_by_class_name('caret').click()
    driver.implicitly_wait(0.5)
    driver.find_element_by_link_text('Cerrar sesion en Netflix').click()
    driver.implicitly_wait(0.5)
    driver.back()




#test_netflix_login(start_connection())
#test_netflix_search(start_connection())
test_netflix_user_selection(start_connection())