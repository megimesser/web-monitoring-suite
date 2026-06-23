import time

# --- Konfiguration ---
from config import TXT_PATH,HAUPTSEITEN_LINKS,UNTERSEITEN_LINKS,UNTERSEITEN_AUSSTELLER,UNTERSEITEN_BESUCHER,TEST_MAIL,TEST_NUMMER,MESSAGE,MESSE_LOOP,MESSE_LOOP_A,GOOGLE_KEY,ACCOUNT,TARGET  # nur das aufzählen, was du hier wirklich nutzt

# --- Seitenaufrufe ---
from seitenaufruf import (
    requester,
    text_writer,
    message_emptyer
)

# --- Gmail ---
from gmail.deleter import delete_all
from gmail.filter import get_service, main_reader

# --- Messe-Workflows ---
from seitennachricht import aussteller, besucher
from karten import messe_looper
from anmeldung import messe_looper_anmeldung

# --- Benachrichtigung ---
from sender import sms_searcher


# --- CMS --- 
from cms.verzeichnis import verzeichnis,counter_cms


from mailing.nachrichten import sender





# Variablendefinition
service = get_service()





# Sender



#Nachrichten im Postfach werden gelöscht
delete_all(service)

#Textdatei wird geleert 
message_emptyer(TXT_PATH, message="")

#Request + in Testdatei schreiben
text_writer(TXT_PATH, requester(HAUPTSEITEN_LINKS))   # Reihenfolge: path, message
text_writer(TXT_PATH, requester(UNTERSEITEN_LINKS))
text_writer(TXT_PATH, requester(UNTERSEITEN_AUSSTELLER))
text_writer(TXT_PATH, requester(UNTERSEITEN_BESUCHER))





# Nachrichten versenden 
aussteller(TEST_MAIL,TEST_NUMMER,MESSAGE)
besucher(TEST_MAIL,TEST_NUMMER,MESSAGE)



# Karten versenden 
messe_looper(TEST_MAIL,MESSE_LOOP)





# Austeller 
messe_looper_anmeldung(TEST_MAIL,MESSE_LOOP_A)
# Fehlersucher 


# cms
counter_cms(verzeichnis())


# warten bis Schnittstellen alle Nachrichten versendet haben 
time.sleep(60)


#SMS - Sender



main_reader()
sms_searcher(TXT_PATH)
sender(GOOGLE_KEY,ACCOUNT,TARGET)