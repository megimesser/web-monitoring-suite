from dotenv import load_dotenv
from twilio.rest import Client
import re
from config import TXT_PATH,AUTH_TOKEN,ACCOUNT_SID,TWILIO_NUMBER,SMS_EMPFAENGER
load_dotenv()


def sms_sender(nachricht, empfaenger):
    #Head twillio

    client = Client(ACCOUNT_SID, AUTH_TOKEN) 
    message = client.messages.create(
        body=nachricht,
        from_=TWILIO_NUMBER,
        to=empfaenger
    )
    print(f"SMS gesendet — SID: {message.sid}")
#test



def sms_searcher(path):
    with open(path,"r") as f:
        daten = f.read()
    x = re.search("fehlgeschlagen", daten)
    print(type(x))
    x = bool(x)
    if x:
        print("gefunden")
        
        sms_sender(nachricht="fehlgeschlagen", empfaenger=SMS_EMPFAENGER)
    #return x
        

if __name__ == '__main__':
    sms_searcher(TXT_PATH)
    print(sms_searcher(TXT_PATH))






#sms_sender(nachricht="hi", empfaenger="+491602986823")


