from encrypter import *
from decrypter import *

def test_encrypt():
    assert encrypt('test_content.txt') == 'encrypted!'

def test_decrypt():
    assert decrypt('test_content.txt.crypted') == 'decrypted!'
