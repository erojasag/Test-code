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
    driver.implicitly_wait(0.5)
    driver.find_element_by_id('id_userLoginId').send_keys(config.username)
    driver.implicitly_wait(0.5)
    driver.find_element_by_id('id_password').send_keys(config.password)
    driver.implicitly_wait(0.5)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    driver.implicitly_wait(4)
    driver.find_element_by_link_text(config.profile).click()
    driver.implicitly_wait(5)

def test_netflix_search(driver):
    driver.implicitly_wait(0.5)
    test_netflix_login(driver)
    driver.implicitly_wait(0.5)
    driver.find_element_by_xpath('//button[@class="searchTab"]').click()
    driver.implicitly_wait(1.5)
    driver.find_element(By.ID,"searchInput").send_keys("Suits")
    driver.implicitly_wait(1.5)

def test_netflix_news(driver):
    driver.implicitly_wait(0.5)
    driver.find_element_by_link_text('Sign In').click()
    driver.implicitly_wait(0.5)
    driver.find_element_by_id('id_userLoginId').send_keys(config.username)
    driver.implicitly_wait(0.5)
    driver.find_element_by_id('id_password').send_keys(config.password)
    driver.implicitly_wait(0.5)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    driver.implicitly_wait(4)
    driver.find_element_by_link_text(config.profile).click()
    driver.implicitly_wait(5)
    driver.find_element_by_link_text('New & Popular').click()
    driver.implicitly_wait(5)

def test_netflix_profile_creation(driver):
    driver.implicitly_wait(0.5)
    driver.implicitly_wait(0.5)
    driver.find_element_by_link_text('Sign In').click()
    driver.implicitly_wait(0.5)
    driver.find_element_by_id('id_userLoginId').send_keys(config.username)
    driver.implicitly_wait(0.5)
    driver.find_element_by_id('id_password').send_keys(config.password)
    driver.implicitly_wait(0.5)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    driver.implicitly_wait(0.5)
    driver.find_element_by_link_text('Add Profile').click()  
    driver.implicitly_wait(2)
    driver.find_element_by_id("add-profile-name").send_keys("Test") 
    driver.implicitly_wait(2)

def test_netflix_logout(driver):
    driver.implicitly_wait(0.5)
    test_netflix_login(driver)
    driver.find_element(By.CLASS_NAME, "caret").click()
    driver.implicitly_wait(0.5)
    driver.find_element(By.CLASS_NAME('sub-menu-link st-hover')).click()
    driver.implicitly_wait(0.5)
    driver.close()




#test_netflix_login(start_connection())
#test_netflix_news(start_connection())
test_netflix_search(start_connection())
#test_netflix_logout(start_connection())
#test_netflix_profile_creation(start_connection())
