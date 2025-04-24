from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


class EncryptionManager:
    def __init__(self):
        self.key = b"\x82,\xc5=\\\xf4pbXy\xa3\xcch\n\x80\x8e\x10\xc2\x86\xd7\xd6\x04\xab\xc9\r\xc6\x89\x19\xd06&\x9f"
        self.nonce = b"<\xaf\x18\xe8\xf5=\xbd\xb5\x19\x9b\xab\x13\r\x84)<"
        aes_context = Cipher(algorithms.AES(self.key), modes.CTR(self.nonce), backend=default_backend())
        self.encryptor = aes_context.encryptor()

    def updateEncryptor(self, plaintext):
        return self.encryptor.update(plaintext)

    def finalizeEncryptor(self):
        return self.encryptor.finalize()

# Создание экземпляра класса для шифрования
manager = EncryptionManager()

# Список исходных сообщений
plaintexts = [
    b"SHORT",
    b"MEDIUM MEDIUM MEDIUM",
    b"LONG LONG LONG LONG LONG LONG"
]

# Шифрование каждого сообщения
ciphertexts = []
for m in plaintexts:
    ciphertexts.append(manager.updateEncryptor(m))

# Запись зашифрованных сообщений в файл
with open("ciphertexts.bin", "wb") as file:
    for ciphertext in ciphertexts:
        file.write(ciphertext)
