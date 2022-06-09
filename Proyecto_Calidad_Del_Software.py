from tracemalloc import start
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import config


def start_connection():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.netflix.com/')
    return driver


def test_netflix_login(driver):
    driver.implicitly_wait(0.5)
    driver.find_element_by_link_text('Sign In').click()
    driver.find_element_by_id('id_userLoginId').send_keys(config.username)
    driver.find_element_by_id('id_password').send_keys(config.password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    driver.implicitly_wait(0.5)
    driver.back()


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



#test_netflix_login(start_connection())
test_netflix_search(start_connection())
