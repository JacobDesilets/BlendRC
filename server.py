from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread


class ServerThread(Thread):
    def __init__(self, port=8888):
        super().__init__()
        self.port = port
        self.is_connected = False
        self.host = '127.0.0.1'

    
    def run(self):
        print('Hello from the server thread!')
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen()
        conn, addr = s.accept()
        print(f'Connected to {addr}')
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            conn.sendall(data)

        print('Goodbye from the server thead!')
        conn.close()
        s.close()
