import socket
import time

HOST = '127.0.0.1' # The server's hostname or IP address
PORT = 1377        # The port used by the server
while True:
    PORT = PORT+1
    if PORT == 1900:
        PORT == 1377
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        s.connect((HOST, PORT))
        while True:
            msg  = input()
            s.sendall(msg.encode())
            data = s.recv(1024)
            message = data.decode() 
            print(f'received {message!r}')
            if msg == 'end':
                break
    time.sleep(1)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        s.bind((HOST, PORT))
        s.listen(10)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr) 
            while True:
                data = conn.recv(1024) 
                if not data:
                    break
                conn.sendall(data)
                print(data)