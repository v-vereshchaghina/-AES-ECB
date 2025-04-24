import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def encrypt_message(message, key): # Шифрование
    # Создание объекта шифра
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor() # Создается объект, который может выполнять шифрование
    # Шифрование сообщения
    encrypted_message = encryptor.update(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message, key):
    # Создается объект шифра
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()

    # Расшифровка сообщения
    decrypted_message = decryptor.update(encrypted_message)
    return decrypted_message.decode()


# Генерация ключа 16 случайных байт (128-битный ключ для AES)
key = os.urandom(16)

# Сообщение для шифрования
message = "Давайте встретимся в кафе у парка"
# Шифрование сообщения
encrypted_message = encrypt_message(message, key)
print("Зашифрованное сообщение:", encrypted_message)

# Дешифрование сообщения
decrypted_message = decrypt_message(encrypted_message, key)
print("Расшифрованное сообщение:", decrypted_message)
