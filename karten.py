from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from Testsuite.config import TEST_MAIL, MESSE_LOOP, VORNAME, NACHNAME


def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service("/usr/bin/chromedriver")
    return webdriver.Chrome(service=service, options=options)


def messe_looper(TEST_MAIL, MESSE_LOOP):
    for messe in MESSE_LOOP:
        freikarte(TEST_MAIL, messe)


def freikarte(TEST_MAIL, messe):
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.wohnbautrend.de/messeticket-formular")

        print(driver.title)

        vorname_input = wait.until(
            EC.presence_of_element_located((By.ID, "Vorname"))
        )
        nachname_input = driver.find_element(By.ID, "Nachname")
        mail_input = driver.find_element(By.ID, "Mail")
        messe_dropdown = driver.find_element(By.ID, "Messe")
        checkbox = driver.find_element(By.ID, "checkbox-2")
        submit = driver.find_element(By.CSS_SELECTOR, ".submit-button-4.w-button")

        vorname_input.send_keys(VORNAME)
        nachname_input.send_keys(NACHNAME)
        mail_input.send_keys(TEST_MAIL)

        Select(messe_dropdown).select_by_visible_text(messe)

        checkbox.click()
        time.sleep(1)
        submit.click()
        time.sleep(5)

    finally:
        driver.quit()


if __name__ == "__main__":
    messe_looper(TEST_MAIL, MESSE_LOOP)