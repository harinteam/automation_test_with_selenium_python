import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.google.com')
    yield driver
    driver.quit()
    time.sleep(60)


def test_googling(driver):
    driver.find_element_by_name('q').send_keys('halrez web dev' + Keys.ENTER)
    assert 'Halrez Web Dev IT' in driver.find_element_by_css_selector('h3').text
    assert 'Halrez Web Dev IT' in driver.title
    # driver.quit()
    # time.sleep(100)
