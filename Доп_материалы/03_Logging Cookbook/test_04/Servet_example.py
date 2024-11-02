# А вот сценарий, который берет имя файла и отправляет этот файл на сервер, правильно предваряя его длину
# в двоичном коде, в качестве новой конфигурации ведения журнала:

import socket, sys, struct

# with open(sys.argv[1], 'rb') as f:
#     data_to_send = f.read()

with open('test.conf', 'rb') as f:
    data_to_send = f.read()

HOST = 'localhost'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('connecting...')
s.connect((HOST, PORT))

print('sending config...')
s.send(struct.pack('>L', len(data_to_send)))
s.send(data_to_send)

s.close()
print('complete')