import os 
from dotenv import load_dotenv


#karten.py 
TEST_MAIL = "testautomationheinze@gmail.com"
VORNAME = "Testautomation"
NACHNAME = "Testautomation"
MESSE_LOOP = ["Messe Duisburg","Messe Kaiserslautern","Messe Moers", "Messe Düren", "Messe Düsseldorf", "Messe Hückelhoven"]


#Seitenaufruf 
HAUPTSEITEN_LINKS= ["https://www.wohnbautrend.de/","https://www.wohnbautrend.de/aussteller-links","https://www.wohnbautrend.de/besucher-links","https://www.wohnbautrend.de/uber-uns","https://www.wohnbautrend.de/aktuelles","https://www.wohnbautrend.de/messeanmeldung","https://www.wohnbautrend.de/messeticket-formular"]
UNTERSEITEN_LINKS = ["https://www.wohnbautrend.de/messeunterseiten/duisburg","https://www.wohnbautrend.de/messeunterseiten/wohn-bau-trend-kaiserslautern","https://www.wohnbautrend.de/messeunterseiten/moers","https://www.wohnbautrend.de/messeunterseiten/dueren","https://www.wohnbautrend.de/messeunterseiten/huckelhoven","https://www.wohnbautrend.de/messeunterseiten/duesseldorf"]
UNTERSEITEN_AUSSTELLER = ["https://www.wohnbautrend.de/ausstellerunterseiten/duisburg-aussteller","https://www.wohnbautrend.de/ausstellerunterseiten/aussteller---wohn-bau-trend-kaiserslautern","https://www.wohnbautrend.de/ausstellerunterseiten/moers-aussteller","https://www.wohnbautrend.de/ausstellerunterseiten/dueren-aussteller","https://www.wohnbautrend.de/ausstellerunterseiten/huckelhoven-aussteller","https://www.wohnbautrend.de/messeunterseiten/duesseldorf"]
UNTERSEITEN_BESUCHER = ["https://www.wohnbautrend.de/besucherunterseiten/duisburg-besucher","https://www.wohnbautrend.de/besucherunterseiten/kaiserslautern-besucher","https://www.wohnbautrend.de/besucherunterseiten/moers-besucher","https://www.wohnbautrend.de/besucherunterseiten/dueren-besucher","https://www.wohnbautrend.de/besucherunterseiten/huckelhoven-besucher","https://www.wohnbautrend.de/besucherunterseiten/duesseldorf-besucher"]
### Functions ###

#seitennachricht.py 
TEST_NUMMER = "01602986882"
MESSAGE = "Dies ist eine automatisch generierte Nachricht zur Testautomation"

#anmeldungen.py
MESSE_LOOP_A = ["Messe Duisburg","Messe Kaiserslautern","Messe Moers", "Messe Düren", "Messe Düsseldorf", "Messe Hückelhoven"]

#filter.py
# --- Pfade relativ zur Skriptdatei, nicht zum Startverzeichnis ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']


# .env-Datei laden (liegt neben der config.py)
load_dotenv(os.path.join(BASE_DIR, '.env'))

SMS_EMPFAENGER = os.environ.get("SMS_EMPFAENGER", "")

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
TOKEN_PATH = os.path.join(BASE_DIR, 'token.json')
CLIENT_PATH = os.path.join(BASE_DIR, 'client.json')
TXT_PATH = os.path.join(BASE_DIR, 'data/Bericht.txt')
#os.path.join(BASE_DIR, 'test.txt')

#filter.py
ERWARTETE_ANZAHL = 14


#sender.py
AUTH_TOKEN = os.environ.get("AUTH_TOKEN", "")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID", "")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER", "")
SMS_EMPFAENGER = os.environ.get("SMS_EMPFAENGER", "")


#verzeichnis.py 
CMS_EINTRÄGE = 149


#nachrichten.py
GOOGLE_KEY = os.environ.get("GOOGLE_KEY","")
ACCOUNT = os.environ.get("ACCOUNT", "")
TARGET = os.environ.get("TARGET","")


#Für Ausführung auf CentOS 
CHROME_BINARY= "/usr/bin/chromium-browser"