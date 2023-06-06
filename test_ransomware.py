from encrypter import *

def test_encrypt():
    assert encrypt('content.txt') == 'encrypted!'
