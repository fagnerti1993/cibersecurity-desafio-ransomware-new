import os
import pyaes

def decrypt_file(encrypted_file_name, key):
    """Descriptografa um arquivo e restaura o nome original."""
    try:
        with open(encrypted_file_name, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()

        # Criar a instância do AES e descriptografar os dados
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypted_data = aes.decrypt(encrypted_data)

        # Nome do arquivo original restaurado
        original_file_name = encrypted_file_name.replace(".ransom", "")

        with open(original_file_name, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)

        # Remover o arquivo criptografado
        os.remove(encrypted_file_name)

        print(f"Arquivo '{encrypted_file_name}' descriptografado com sucesso!")
        print(f"Arquivo original restaurado como '{original_file_name}'")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{encrypted_file_name}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {e}")

if __name__ == "__main__":
    encrypted_file_name = "teste.txt.ransom"
    key = b"testeransomwares"

    decrypt_file(encrypted_file_name, key)
