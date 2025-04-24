from threading import Thread
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


def keystream(method, iteration):
    # Генерация ключа и IV
    key = os.urandom(32)
    iv = os.urandom(16)

    # Выбор метода шифрования
    if method == 'CTR':
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    else:
        raise ValueError("Unsupported method")

    encryptor = cipher.encryptor()

    # Генерация потока ключей
    keystream_blocks = []
    for _ in range(iteration):
        keystream_blocks.append(encryptor.update(b"\x00" * 16))  # Генерация блока потока ключей размером 16 байт

    return keystream_blocks


# Количество блоков для генерации
iteration = 10

# Создание и запуск потоков
t1 = Thread(target=keystream, args=('CTR', iteration))
t2 = Thread(target=keystream, args=('CTR', iteration))

t1.start()
t2.start()

t1.join()
t2.join()


# 1) Определяет функцию keystream, которая принимает метод шифрования и количество итераций для генерации потока ключей.
# 2) Внутри функции выбирается соответствующий метод шифрования (в данном случае только CTR) и создаются объекты для шифрования.
# 3) Для каждой итерации генерируется блок потока ключей размером 16 байт.
# 4) Создаются два потока t1 и t2, которые независимо друг от друга вызывают функцию keystream с методом CTR и заданным количеством итераций.
# 5) Поток t1 и t2 запускаются и дожидаются завершения с помощью метода join.

