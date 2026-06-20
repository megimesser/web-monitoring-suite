from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from Testsuite.config import TEST_MAIL, MESSE_LOOP_A


def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service("/usr/bin/chromedriver")
    return webdriver.Chrome(service=service, options=options)


def messe_looper_anmeldung(TEST_MAIL, MESSE_LOOP_A):
    for messe in MESSE_LOOP_A:
        anmeldung(TEST_MAIL, messe)


def anmeldung(TEST_MAIL, messe):
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.wohnbautrend.de/messeanmeldung-formular")

        print(driver.title)
        print(messe)

        ansprechpartner_input = wait.until(
            EC.presence_of_element_located((By.ID, "Ansprechpartner"))
        )
        unternehmen_input = driver.find_element(By.ID, "Unternehmen")
        branche_dropdown = driver.find_element(By.ID, "Branche")
        mail_input = driver.find_element(By.ID, "Email-4")
        number_input = driver.find_element(By.ID, "Telefonnummer")
        message_input = driver.find_element(By.ID, "Nachricht")
        messe_dropdown = driver.find_element(By.ID, "Messeauswahl")
        checkbox = driver.find_element(By.ID, "Aussteller")
        submit = driver.find_element(By.ID, "submitter")

        ansprechpartner_input.send_keys("Testautomation")
        unternehmen_input.send_keys("Testautomation")

        Select(branche_dropdown).select_by_visible_text("Camping")

        mail_input.send_keys(TEST_MAIL)
        number_input.send_keys("01602986822")
        message_input.send_keys("Dies ist ein automatisches Testscript")

        Select(messe_dropdown).select_by_visible_text(messe)

        checkbox.click()
        submit.click()

        time.sleep(2)

    finally:
        driver.quit()


if __name__ == "__main__":
    messe_looper_anmeldung(TEST_MAIL, MESSE_LOOP_A)