from selenium import webdriver
import time
import requests
import os 
from dotenv import load_dotenv
from Testsuite.config import HAUPTSEITEN_LINKS, UNTERSEITEN_LINKS,UNTERSEITEN_AUSSTELLER,UNTERSEITEN_BESUCHER,TXT_PATH



### Functions ###

def message_emptyer(path,message):
    with open(path,"w") as f:
        f.writelines(message)


def text_writer(path, message):
    with open(path, "a") as f:
        f.writelines(message)


def requester(links):
    

    message_string = ""                         # vor der Schleife
    seiten_erreichbar = 0

    for i in links:

        # Für Identifikatin im Bericht 
        if i == "https://www.wohnbautrend.de/":
            message_string += "\n\n ⭐HAUPTSEITEN⭐\n"
        elif i == "https://www.wohnbautrend.de/messeunterseiten/duisburg":
            message_string += "\n\n ⭐ MESSEUNTERSEITEN⭐\n"
        elif i == "https://www.wohnbautrend.de/ausstellerunterseiten/duisburg-aussteller":
            message_string += "\n\n ⭐AUSSTELLERSEITEN⭐\n"
        elif i == "https://www.wohnbautrend.de/besucherunterseiten/duisburg-besucher":
            message_string +=  "\n\n⭐ BESUCHERUNTERSEITEN⭐\n"

        response = requests.get(i)
        if response.status_code == 200:
            print(f"✅ Status {response.status_code} — Seite erreichbar")
            driver = webdriver.Chrome()
            driver.get(i)
            titel = driver.title                # titel VORHER speichern
            print(f"Titel: {titel}")
            time.sleep(10)
            driver.quit()                       # jetzt erst beenden
            seiten_erreichbar += 1
            message_string += f"✅ Status {response.status_code} — Seite erreichbar\n"
            message_string += f"Titel: {titel}\n"
        else:
            print(f"❌ Status {response.status_code} — Seitenaufruf fehlgeschlagen")
            message_string += f"❌ Status {response.status_code} — fehlgeschlagen\n"
            #message_string += f"Titel: {titel}\n"
    
    seiten_erreichbar = int(seiten_erreichbar)

    return message_string


### Function callingd ### 

if __name__ == "__main__":
    message_emptyer(TXT_PATH, message="")
    ergebnis = requester(HAUPTSEITEN_LINKS)
    text_writer(TXT_PATH, ergebnis)