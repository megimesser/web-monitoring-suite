from selenium.webdriver.common.by import By
import time
from config import CMS_EINTRÄGE, SMS_EMPFAENGER, TXT_PATH
from sender import sms_sender
from driver_setup import get_driver



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