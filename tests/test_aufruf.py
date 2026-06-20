#import

from seitenaufruf import message_emptyer, text_writer, requester

# Mocks für Requests
from unittest.mock import patch, Mock


#Hinweise 
"""
 # Arrange – Vorbereitung
    datei = tmp_path / "test.txt"
    inhalt = "Hallo Welt"

    # Act – die Funktion ausführen
    message_emptyer(datei, inhalt)

    # Assert – prüfen ob das Ergebnis stimmt

"""


# Seitenaufruf Tests
# assert Prüft Bedingunen auf True oder False

def test_message_emptyer(tmp_path):
    datei = tmp_path / "test.txt"
    message_emptyer(datei, "Hallo")
    assert datei.read_text() == "Hallo"


def test_text_writer(tmp_path):
    datei = tmp_path / "test.txt"
    text_writer(datei,"Hallo")
    assert datei.read_text() 


# requests mit Mockdaten ausführen
# Wichtig - eine Funktion die mehrere Dinge tu ist schwer testbar 


def test_requester_status_200():
    fake_response = Mock()
    fake_response.status_code = 200

    with patch("seitenaufruf.requests.get", return_value=fake_response):
        ergebnis = requester(["https://www.wohnbautrend.de/"])    # Liste, eckige Klammern

    assert "✅ Status 200 — Seite erreichbar" in ergebnis