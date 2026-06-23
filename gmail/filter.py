from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import re
from sender import sms_sender
from config import TOKEN_PATH, SCOPES, CLIENT_PATH,ERWARTETE_ANZAHL,TXT_PATH,SMS_EMPFAENGER


def get_service():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'w') as f:
            f.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)


def get_all_message_ids(service, query=None):
    ids = []
    page_token = None
    while True:
        resp = service.users().messages().list(
            userId='me',
            maxResults=500,
            pageToken=page_token,
            q=query
        ).execute()

        ids.extend(m['id'] for m in resp.get('messages', []))

        page_token = resp.get('nextPageToken')
        if not page_token:
            break
    return ids


def has_relevant_attachment(msg):
    """Prüft rekursiv alle Parts der Mail auf PDF- oder JPG-Anhänge."""

    def check_parts(parts):
        for part in parts:
            filename = part.get('filename', '').lower()
            mime = part.get('mimeType', '')
            if filename.endswith(('.pdf', '.jpg')) or mime == 'application/pdf':
                return True
            if check_parts(part.get('parts', [])):
                return True
        return False

    return check_parts(msg['payload'].get('parts', []))


# Prüfung Anzahl der Nachrichten
def counter(anzahl):
    if anzahl != ERWARTETE_ANZAHL:
        meldung = "Fehler : vorhandene Anzahl ist nicht korrekt - EMAIL"
        print(meldung)
        sms_sender(nachricht=meldung, empfaenger=SMS_EMPFAENGER)
    else:
        print("anzahl korrekt")


def text_writer(message, path=TXT_PATH):
    with open(path, "a") as f:
        f.write(message)


def main_reader():
    helper_3 = True
    helper_2 = True
    service = get_service()
    message_string = ""

    # q=None holt ALLE Mails. Zum Filtern z.B. q='is:unread' oder q='newer_than:7d'
    message_ids = get_all_message_ids(service, query=None)
    print(f'{len(message_ids)} Nachrichten gefunden')
    counter(len(message_ids))

    for mid in message_ids:
        msg = service.users().messages().get(
            userId='me', id=mid, format='full'
        ).execute()

        headers = {h['name']: h['value'] for h in msg['payload'].get('headers', [])}
        subject = headers.get('Subject', '(kein Betreff)')

        # Prüfung Anmeldedaten + Karten (gleiche Logik, ein Block)
        if re.search(r"^(Ihre|Dein)", subject) and has_relevant_attachment(msg):
            if helper_2:
                message_string += "\n\n⭐ Tickets / Anmeldungen ⭐\n"
                helper_2 = False 
            f = subject.split()
            text = f"{f[1]} {f[-1]} in Ordnung ✅ "
            print(text)
            message_string += f"{text} \n"

        # Prüfung Nachrichten
        if re.search(r"Webseite :", subject):
            if helper_3:
                message_string += "\n\n⭐ Aussteller / Besuchernachricht ⭐\n"
                helper_3 = False
            text = f"{subject.split()[-1]} wird versendet ✅"
            print(text)
            helper_3 = False
            message_string += f"{text} \n"

    text_writer(message_string)


if __name__ == '__main__':
    main_reader()