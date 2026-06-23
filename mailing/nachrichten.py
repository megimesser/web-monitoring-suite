#!/usr/bin/env python3
import smtplib
from email.message import EmailMessage
from datetime import datetime 
from config import GOOGLE_KEY,TXT_PATH,ACCOUNT,TARGET


def sender(GOOGLE_KEY, ACCOUNT, TARGET):

    with open (TXT_PATH , "r") as file:
        context = file.read()
    print(context)

    # Datum in kurzes Format bringen 
    time = datetime.today()
    time=str(time)
    cut_datum = time[0:10]
    print(cut_datum)

    #GOOGLE_KEY = os.getenv("GOOGLE_KEY")
    GOOGLE_KEY=str(GOOGLE_KEY)
    

    
    

    msg = EmailMessage()
    msg["Subject"] = f" Testbericht für den {cut_datum}"
    msg["From"] = ACCOUNT
    msg["To"] = TARGET

    msg.set_content(context)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(ACCOUNT, GOOGLE_KEY)
        smtp.send_message(msg)
    print("fertig")



if __name__ == "__main__":
    sender(GOOGLE_KEY,ACCOUNT,TARGET)
    
