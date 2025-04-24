from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os


class EncryptionManager:
    def __init__(self):
        self.key = os.urandom(32)
        self.iv = os.urandom(16)

    def encrypt_message(self, message):
        encryptor = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend()).encryptor()
        padder = padding.PKCS7(128).padder()
        padded_message = padder.update(message)
        padded_message += padder.finalize()
        ciphertext = encryptor.update(padded_message)
        ciphertext += encryptor.finalize()
        return ciphertext

    def decrypt_message(self, ciphertext):
        decryptor = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend()).decryptor()
        unpadder = padding.PKCS7(128).unpadder()
        padded_message = decryptor.update(ciphertext)
        padded_message += decryptor.finalize()
        message = unpadder.update(padded_message)
        message += unpadder.finalize()
        return message


# Создание экземпляра класса для шифрования/дешифрования
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
    ciphertexts.append(manager.encrypt_message(m))

# Зашифрованные сообщения
for c in ciphertexts:
    print("Шифртекст:", c)

# Расшифровываем и проверяем
for c in ciphertexts:
    print("Расшифрованное сообщение:", manager.decrypt_message(c))

# При каждом запуске программы с одинаковыми входными данными будут получаться разные шифртексты,
# даже если используется один и тот же ключ и IV.В режиме CBC каждый блок шифруется с учетом предыдущего блока,
# что делает шифртекст уникальным для каждого запуска.

