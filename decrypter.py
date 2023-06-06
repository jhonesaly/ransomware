import os
import pyaes

def decrypt(file_name):
    ## abrir o arquivo criptografado
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()

    ## chave para descriptografia
    key = b"senharesgate1111"
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    ## remover o arquivo criptografado
    os.remove(file_name)

    ## criar o arquivo descriptografado
    new_file = file.replace(".crypted", "")
    new_file = open(f'{new_file}', "wb")
    new_file.write(decrypt_data)
    new_file.close()
    return 'decrypted!'
