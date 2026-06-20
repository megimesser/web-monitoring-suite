from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
import os
#from gmail.reader import get_service



SCOPES = ['https://www.googleapis.com/auth/gmail.modify']


def get_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as f:
            f.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)



def get_all_message_ids(service):
    ids = []
    page_token = None
    while True:
        resp = service.users().messages().list(
            userId='me',
            maxResults=500,
            pageToken=page_token
        ).execute()
        ids.extend(m['id'] for m in resp.get('messages', []))
        page_token = resp.get('nextPageToken')
        if not page_token:
            break
    return ids


def delete_all(service):
    message_ids = get_all_message_ids(service)
    print(f'{len(message_ids)} Nachrichten gefunden')

    for i, mid in enumerate(message_ids, 1):
        service.users().messages().trash(userId='me', id=mid).execute()
        print(f'[{i}/{len(message_ids)}] gelöscht')

    return len(message_ids)


if __name__ == '__main__':
    service = get_service()
    delete_all(service)