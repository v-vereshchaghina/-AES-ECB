import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import sys

# Генерируется 256-битный ключ для AES (32 байта)
key = os.urandom(32)

# Создание объекта шифра
aesCipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
aesEncryptor = aesCipher.encryptor()

# Получение имен файлов из аргументов командной строки
# ifile, ofile = sys.argv[1:3]

# Исходный файл
ifile = '123.jpeg'
# Файл в которой записано зашифрованное изображение
ofile = '321.jpeg'

with open(ifile, "rb") as reader:
    # Чтение данных файла
    image_data = reader.read()
    # Разделение данных на заголовок (первые 54 байта) и всё остальное
    header, body = image_data[:54], image_data[54:]
    # Дополняем тело чтобы его длина была кратна 16 байт - размеру блока AES
    body += b"\x00" * (16 - (len(body) % 16))

    with open(ofile, "wb+") as writer:
        # Запись заголовка и зашифрованного тела в новый файл
        writer.write(header + aesEncryptor.update(body))
