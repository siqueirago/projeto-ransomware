import os
from cryptography.fernet import Fernet

PASTA_ARQUIVOS = "files"

def gerar_chave():
    if not os.path.exists("chave.key"):
        chave = Fernet.generate_key()
        with open("chave.key", "wb") as chave_file:
            chave_file.write(chave)

def carregar_chave():
    return open("chave.key", "rb").read()

def criptografar_arquivo(caminho):
    chave = carregar_chave()
    f = Fernet(chave)

    with open(caminho, "rb") as file:
        dados = file.read()

    dados_criptografados = f.encrypt(dados)

    with open(caminho, "wb") as file:
        file.write(dados_criptografados)

def criptografar_pasta():
    for arquivo in os.listdir(PASTA_ARQUIVOS):
        caminho = os.path.join(PASTA_ARQUIVOS, arquivo)
        if os.path.isfile(caminho):
            criptografar_arquivo(caminho)
            print(f"Criptografado: {arquivo}")

if __name__ == "__main__":
    gerar_chave()
    criptografar_pasta()
    print("\nTodos os arquivos foram criptografados!")