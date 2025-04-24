from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


class DecryptionManager:
    def __init__(self):
        # Тот же ключ, что и при шифровании
        self.key = b"\x82,\xc5=\\\xf4pbXy\xa3\xcch\n\x80\x8e\x10\xc2\x86\xd7\xd6\x04\xab\xc9\r\xc6\x89\x19\xd06&\x9f"
        # Тот же nonce, что и при шифровании
        self.nonce = b"<\xaf\x18\xe8\xf5=\xbd\xb5\x19\x9b\xab\x13\r\x84)<"
        aes_context = Cipher(algorithms.AES(self.key), modes.CTR(self.nonce), backend=default_backend())
        self.decryptor = aes_context.decryptor()

    def updateDecryptor(self, ciphertext):
        return self.decryptor.update(ciphertext)

    def finalizeDecryptor(self):
        return self.decryptor.finalize()


# Чтение зашифрованных сообщений из файла
with open("ciphertexts.bin", "rb") as file:
    ciphertexts = file.read()

# Дешифрование сообщений
manager = DecryptionManager()
plaintexts = manager.updateDecryptor(ciphertexts)

print("Расшифрованные сообщения:", plaintexts)
