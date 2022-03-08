import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_googling():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.google.com')
    driver.find_element_by_name('q').send_keys('Home Official Chelsea FC' + Keys.ENTER)
    assert 'Home | Official Site | Chelsea Football Club' in driver.find_element_by_css_selector('h3').text
    assert 'Home | Official Site | Chelsea Football Club' in driver.title
    driver.quit()
