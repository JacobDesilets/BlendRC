from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread


class ServerThread(Thread):
    def __init__(self, host, port):
        super().__init__()
        self.port = port
        self.is_connected = False
        self.host = host
        self.stop = False
        self.socket = socket(AF_INET, SOCK_STREAM)

    
    def run(self):
        print('Hello from the server thread!')
        self.socket.bind((self.host, int(self.port)))
        self.socket.listen()
        try:
            conn, addr = self.socket.accept()
        except:
            print('Server thread brutally murdered :(')
            return
        print(f'Connected to {addr}')
        while not self.stop:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            conn.sendall(data)

        print('Goodbye from the server thead!')
        conn.close()
        self.socket.close()

    def quit(self):
        self.stop = True
        self.socket.close()
