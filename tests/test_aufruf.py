#import

from seitenaufruf import message_emptyer




# Seitenaufruf Tests

def test_message_emptyer(tmp_path):
    datei = tmp_path / "test.txt"
    message_emptyer(datei, "Hallo")
    assert datei.read_text() == "Hallo"