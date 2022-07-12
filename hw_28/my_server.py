import socket
import select
from datetime import datetime
from random import randint


def read_log():
    with open('log_hist.txt') as file:
        return ' '.join(file.readlines())


class Server:
    _INPUTS = []
    _OUTPUTS = []
    _MESSAGES = {}
    _SERVER_SOCK: socket = None
    _SERVER_RESP = {
        'GET': {
            'C': f'TEMP {randint(50, 110)} С',
            'F': f'TEMP {(randint(50, 110) * 9 / 5) + 32} F',
            'DATE': f'{datetime.now().date()}',
            'TIME': f'{datetime.now().time()}',
            'DATATIME': f'{datetime.now()}',
            'HIST': f'{read_log()}',
        },
    }

    def __init__(self, host: str = 'localhost', port: int = 9090, cli_scope: int = 5):
        self.host = host
        self.port = port
        self.cli_scope = cli_scope
        self._log = None

    def run(self):
        self._SERVER_SOCK = socket.socket()
        self._SERVER_SOCK.bind((self.host, self.port))
        self._SERVER_SOCK.listen(self.cli_scope)
        self._SERVER_SOCK.setblocking(False)
        self._INPUTS.append(self._SERVER_SOCK)
        self._start_server()

    def _wait_cli_or_data(self):
        reads, send, excepts = select.select(self._INPUTS, self._OUTPUTS, self._INPUTS)
        for conn in reads:
            if conn == self._SERVER_SOCK:
                new_cli_conn, client_addr = conn.accept()
                print(f'Client connected on {client_addr[1]} port...!')
                new_cli_conn.setblocking(False)
                self._INPUTS.append(new_cli_conn)
            else:

                data = conn.recv(1024)
                if data:
                    if self._MESSAGES.get(conn, None):
                        self._MESSAGES[conn].append(data)
                    else:
                        self._MESSAGES[conn] = [data]
                    self._OUTPUTS.append(conn) if conn not in self._OUTPUTS else ...
                else:
                    print('Client disconnected...')
                    self._OUTPUTS.remove(conn) if conn in self._OUTPUTS else ...
                    self._INPUTS.remove(conn)
                    conn.close()
                    del self._MESSAGES[conn]

    def _send_message(self):
        reads, send, excepts = select.select(self._INPUTS, self._OUTPUTS, self._INPUTS)
        for conn in send:
            msg = self._MESSAGES.get(conn, None)
            if len(msg):
                temp = msg.pop(0).decode('utf-8')
                method_key, info_key, cli_port = temp.split(' ')
                err = 'Wrong request...!'
                try:
                    resp = self._SERVER_RESP[method_key][info_key]
                    self._log_req(cli_port=cli_port, data=resp)
                    conn.send(resp.encode('utf-8'))
                except KeyError:
                    conn.send(err.encode('utf-8'))
            else:
                self._OUTPUTS.remove(conn)

    def _handle_exception(self):
        reads, send, excepts = select.select(self._INPUTS, self._OUTPUTS, self._INPUTS)
        for conn in excepts:
            print('Client disconnected with error...')
            self._INPUTS.remove(conn)
            if conn in self._OUTPUTS:
                self._OUTPUTS.remove(conn)
            conn.close()
            del self._MESSAGES[conn]

    def _start_server(self):
        try:
            print('Server is running...!\n')
            while True:
                self._wait_cli_or_data()
                self._send_message()
                self._handle_exception()
        except KeyboardInterrupt:
            print('\nBye')

    @staticmethod
    def _log_req(cli_port: int, data: str):
        with open('log_hist.txt', 'a') as file:
            file.write(f'{cli_port} - {str(datetime.now())} - {data}\n')


def main():
    user_params = input('\nEnter host and port: ')
    if user_params:
        us_host, us_port = user_params.split(' ')
        server = Server(us_host, us_port)
    else:
        server = Server()
    server.run()


if __name__ == '__main__':
    main()
