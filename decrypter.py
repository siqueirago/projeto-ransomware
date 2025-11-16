
import os
from cryptography.fernet import Fernet

PASTA_ARQUIVOS = "files"

def carregar_chave():
    return open("chave.key", "rb").read()

def descriptografar_arquivo(caminho):
    chave = carregar_chave()
    f = Fernet(chave)

    with open(caminho, "rb") as file:
        dados_criptografados = file.read()

    dados = f.decrypt(dados_criptografados)

    with open(caminho, "wb") as file:
        file.write(dados)

def descriptografar_pasta():
    for arquivo in os.listdir(PASTA_ARQUIVOS):
        caminho = os.path.join(PASTA_ARQUIVOS, arquivo)
        if os.path.isfile(caminho):
            descriptografar_arquivo(caminho)
            print(f"Descriptografado: {arquivo}")

if __name__ == "__main__":
    descriptografar_pasta()
    print("\nTodos os arquivos foram descriptografados!")