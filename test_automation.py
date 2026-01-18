import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    sv = Service("/Users/mac/Repos/cicddemo/chromedriver")
    driver = webdriver.Chrome(service=sv)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()

def test_text_box(driver):
    #step 1
    driver.get("https://demoqa.com/text-box")
    # assert
    
    #step 2
    name_box = driver.find_element(By.XPATH, '//input[@id="userName"]')
    name_box.send_keys("Test Elek")
    
    #step 3
    email_box = driver.find_element(By.ID, 'userEmail')
    email_box.send_keys('test_elek@email.com')

    #step 4
    address_box = driver.find_element(By.XPATH, '//*[@id="currentAddress"]')
    address_box.send_keys('Current address')

    #step 5
    permanent_address_box = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[4]/div[2]/textarea')
    permanent_address_box.send_keys('Permanent address')

    time.sleep(3)

    #step 6
    button = driver.find_element(By.XPATH, '//*[@id="submit"]')
    button.click()

    wait = WebDriverWait(driver, 10)
    nameLabel = wait.until(EC.presence_of_element_located((By.ID, "name")))
    assert "Test Elek" in nameLabel.text

    emailLabel = wait.until(EC.presence_of_element_located((By.ID, "email")))
    assert 'test_elek@email.com' in emailLabel.text

    time.sleep(5)

# /html/body/div[2]/div/div/div/div[2]/div[2]/form/div[1]/div[2]/input

# //input[@id="userName"]