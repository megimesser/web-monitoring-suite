from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

from Testsuite.config import TEST_MAIL, TEST_NUMMER, MESSAGE


def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service("/usr/bin/chromedriver")
    return webdriver.Chrome(service=service, options=options)


def aussteller(TEST_MAIL, TEST_NUMMER, MESSAGE):
    driver = get_driver()
    driver.implicitly_wait(10)

    try:
        driver.get("https://www.wohnbautrend.de")
        print(driver.title)

        name = driver.find_element(By.CSS_SELECTOR, ".w-input")
        mail = driver.find_element(By.CSS_SELECTOR, ".text-field-2.w-input")
        nummer = driver.find_element(By.CSS_SELECTOR, ".spacer-form.w-input")
        nachricht = driver.find_element(By.ID, "Ihre-Nachricht")
        confirm = driver.find_element(By.ID, "checkbox-2")
        dropdown = driver.find_element(By.ID, "Sie-sind")
        submit = driver.find_element(By.CSS_SELECTOR, ".submit-button.w-button")

        name.send_keys("Testautomation")
        mail.send_keys(TEST_MAIL)
        nummer.send_keys(TEST_NUMMER)
        Select(dropdown).select_by_visible_text("Aussteller")
        nachricht.send_keys(MESSAGE)
        confirm.click()
        submit.click()
        time.sleep(5)
    finally:
        driver.quit()


def besucher(TEST_MAIL, TEST_NUMMER, MESSAGE):
    driver = get_driver()
    driver.implicitly_wait(10)

    try:
        driver.get("https://www.wohnbautrend.de")
        print(driver.title)

        name = driver.find_element(By.CSS_SELECTOR, ".w-input")
        mail = driver.find_element(By.CSS_SELECTOR, ".text-field-2.w-input")
        nummer = driver.find_element(By.CSS_SELECTOR, ".spacer-form.w-input")
        nachricht = driver.find_element(By.ID, "Ihre-Nachricht")
        confirm = driver.find_element(By.ID, "checkbox-2")
        dropdown = driver.find_element(By.ID, "Sie-sind")
        submit = driver.find_element(By.CSS_SELECTOR, ".submit-button.w-button")

        name.send_keys("Testautomation")
        mail.send_keys(TEST_MAIL)
        nummer.send_keys(TEST_NUMMER)
        Select(dropdown).select_by_visible_text("Besucher")
        nachricht.send_keys(MESSAGE)
        confirm.click()
        submit.click()
        time.sleep(5)
    finally:
        driver.quit()


if __name__ == "__main__":
    aussteller(TEST_MAIL, TEST_NUMMER, MESSAGE)
    besucher(TEST_MAIL, TEST_NUMMER, MESSAGE)