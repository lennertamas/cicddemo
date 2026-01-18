import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

@pytest.fixture
def driver():
    s = Service('/Users/mac/Repos/cicddemo/chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_text_box_form(driver):
    driver.get("https://demoqa.com/text-box")

    # Várjuk meg, hogy a mezők megjelenjenek
    name_field = driver.find_element(By.ID, "userName")
    email_field = driver.find_element(By.ID, "userEmail")
    current_address_field = driver.find_element(By.ID, "currentAddress")
    permanent_address_field = driver.find_element(By.ID, "permanentAddress")
    submit_button = driver.find_element(By.ID, "submit")

    # Teszt adatok
    name = "Teszt Elek"
    email = "teszt@valami.hu"
    current_address = "1234 Budapest, Teszt utca 1."
    permanent_address = "5678 Szeged, Teszt tér 2."

    # Mezők kitöltése
    name_field.send_keys(name)
    email_field.send_keys(email)
    current_address_field.send_keys(current_address)
    permanent_address_field.send_keys(permanent_address)

    # Submit

    submit_button.click()

    wait = WebDriverWait(driver, timeout=5)
    # Eredmények ellenőrzése
    output_name = wait.until(EC.presence_of_element_located((By.ID, "name"))).text
    output_email = driver.find_element(By.ID, "email").text

    assert name in output_name
    assert email in output_email
