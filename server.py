from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

from . import input


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

        to_send = ''

        while not self.stop:
            data = conn.recv(1024)

            i = input.Input(data.decode())
            if not i.valid:
                to_send = 'INVALID\n'
            else:
                input.input_queue.put(i)
                to_send = ''

            # print(data.decode())
            # if data.decode().strip() == 'STOP':
            #     break

            if to_send:
                conn.sendall(to_send.encode())

        print('Goodbye from the server thead!')
        conn.close()
        self.socket.close()

    def quit(self):
        self.stop = True
        self.socket.close()
