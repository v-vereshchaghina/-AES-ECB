import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Шифрование
def encrypt_message(message, key):
    # Создание объекта шифра
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    # Шифрование сообщения
    encrypted_message = encryptor.update(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message, key):
    # Создание объекта шифра
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()

    # Расшифровка сообщения
    decrypted_message = decryptor.update(encrypted_message)
    return decrypted_message.decode()

# Генерация ключа
key = os.urandom(16)

# Первое сообщение
message1 = "Боб и Алиса встречаются в кафе у парка в 14:00 11 марта.   "
encrypted_message1 = encrypt_message(message1, key)

# Второе сообщение
message2 = "Боб и Алиса встречаются в ресторане у озера в 18:00 15 апреля.      "
encrypted_message2 = encrypt_message(message2, key)

# Замена последнего блока второго зашифрованного сообщения на последний блок первого
block_size = 16  # Размер блока для AES
last_block_index = len(encrypted_message2) - block_size
encrypted_message2_modified = encrypted_message2[:last_block_index] + encrypted_message1[-block_size:]

# Расшифровываем измененное сообщение
decrypted_message2 = decrypt_message(encrypted_message2_modified, key)
print("Расшифрованное сообщение:", decrypted_message2)
