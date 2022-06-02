from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import config

def test_chrome_driver_manager():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://google.com')
    title = driver.title
    assert 'Google' in title # AssertionError: 'Google' not in 'Google'
    
    driver.implicitly_wait(0.5)
    
    search_box = driver.find_element(by= By.NAME, value="q")
    search_button = driver.find_element(by= By.NAME, value="btnK")

    search_box.send_keys('The Big Bang Theory')
    search_button.click()

    search_box = driver.find_element(by=By.NAME, value="q")
    value =search_box.get_attribute('value')
    assert 'The Big Bang Theory' in value # AssertionError: 'The Big Bang Theory' not in 'The Big Bang Theory'
    driver.quit()   # close the browser window

def test_netflix_login():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.netflix.com/')
    driver.implicitly_wait(0.5)
    driver.find_element_by_link_text('Sign In').click()
    driver.find_element_by_id('id_userLoginId').send_keys(config.username)
    driver.find_element_by_id('id_password').send_keys(config.password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    driver.implicitly_wait(0.5)
  # close the browser window


test_netflix_login()
#test_chrome_driver_manager()