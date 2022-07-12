import socket


class Client:

    def __init__(self, host: str = 'localhost', port: int = 9090):
        self.host = host
        self.port = port

    def connect_to_server(self):
        print('For exit enter: `exit`, `quit` или `q`.')
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                while True:
                    port = s.getsockname()[1]
                    mess = f'{input("Enter something >>> ")} {port}'
                    if any(mess.lower() in ext for ext in ['quit', 'exit', 'q']):
                        break
                    mess = mess.encode('utf-8')
                    s.sendall(mess)
                    data = s.recv(1024)
                    print('\nReceived: ', data.decode('utf-8'))
        except KeyboardInterrupt:
            print('\nBye')


if __name__ == '__main__':
    client = Client()
    client.connect_to_server()
