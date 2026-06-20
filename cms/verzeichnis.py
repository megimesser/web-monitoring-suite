from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Testsuite.config import CMS_EINTRÄGE, SMS_EMPFAENGER, TXT_PATH
from Testsuite.sender import sms_sender


def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    return driver


def zaehle_items(driver):
    x = driver.execute_script(
        "return document.querySelectorAll('.w-dyn-item').length"
    )
    return int(x)


def verzeichnis():
    driver = get_driver()
    try:
        driver.get("https://www.wohnbautrend.de/ausstellerverzeichnis")
        datenbankeintraege = 0

        driver.find_element(By.ID, "radio-kl").click()
        print("Filter 'kl' geklickt")
        time.sleep(2)
        datenbankeintraege += zaehle_items(driver)
        print(f"{zaehle_items(driver)} Items nach Filter 'kl'")

        driver.refresh()
        driver.find_element(By.ID, "radio-mo").click()
        print("Filter 'mo' geklickt")
        time.sleep(2)
        print(f"{zaehle_items(driver)} Items nach Filter 'mo'")
        datenbankeintraege += zaehle_items(driver)

        return datenbankeintraege
    finally:
        driver.quit()


def counter_cms(anzahl):
    if anzahl != CMS_EINTRÄGE:
        meldung = "Fehler : vorhandene Anzahl ist nicht korrekt - CMS"
        print(meldung)
        sms_sender(nachricht=meldung, empfaenger=SMS_EMPFAENGER)
        text_writer(meldung)
    else:
        print("anzahl korrekt")
        meldung_2 = f"\n\n⭐CMS⭐ \n✅ {anzahl} / {CMS_EINTRÄGE} Einträge sind innerhalb des Ausstellerverzeichnisses vorhanden"
        text_writer(meldung_2)


def text_writer(message, path=TXT_PATH):
    with open(path, "a") as f:
        f.write(message)


if __name__ == "__main__":
    counter_cms(verzeichnis())