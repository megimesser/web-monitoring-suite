import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def get_service():
    creds = None

    # 1. Schon ein Token vorhanden? -> laden
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # 2. Kein gültiges Token -> refreshen oder neu einloggen
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # 3. Token (neu) speichern – nur in diesem Zweig nötig
        with open('token.json', 'w') as f:
            f.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)


if __name__ == "__main__":
    service = get_service()
    # kurzer Test: Profil abrufen
    profile = service.users().getProfile(userId='me').execute()
    print(f"Verbunden als: {profile['emailAddress']}")
    print(f"Mails gesamt: {profile['messagesTotal']}")