import socket

def Transceive_to_receiver():
    try:
        message_size = 4
        data = b''
        while len(data) < message_size:
            data += transceiver.recv(4096)
        packed_msg_size = data[:message_size]
        msg_size = int.from_bytes(packed_msg_size, byteorder='little')
        print(data)
        while len(data) < msg_size:
            data += transceiver.recv(4096)
        print(data)
        receiver.sendall(data)    
        print('трафик отправлен')
        return None
        
    except:
        print('системная ошибка')
        server_socket_r.close()
        server_socket_t.close()

def Transceive_to_transceiver(a):
    message = a
    if b' ' == message:
        transceiver.sendall(b' ') 
    if b'0' == message:
        transceiver.sendall(b'0')

    
def Waiting():
    while True:
        print('2')
        a = b'1'
        a = receiver.recv(4096)
        print('3')
        if b' ' == a:
            Transceive_to_transceiver(a)
            print('4')
            Transceive_to_receiver()
        if b'0' == a:
            Transceive_to_transceiver(a)
            server_socket_r.close()
            server_socket_t.close()
            return None
        print('1')
            

SERVER_IP_R = '0.0.0.0'  # ip сервера
PORT_R = 22222           # Порт для соединения
SERVER_IP_T = '0.0.0.0'  # ip сервера
PORT_T = 11111           # Порт для соединения
server_socket_r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket_r.bind((SERVER_IP_R, PORT_R))
server_socket_r.listen(1)
print('Ожидание соединения...')
receiver, addr_r = server_socket_r.accept()
print(f'Соединено с {addr_r}')
server_socket_t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket_t.bind((SERVER_IP_T, PORT_T))
server_socket_t.listen(1)
print('Ожидание соединения...')
transceiver, addr_t = server_socket_t.accept()
print(f'Соединено с {addr_t}')
Waiting()