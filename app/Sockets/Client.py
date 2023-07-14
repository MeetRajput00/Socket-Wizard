import socket

class Client:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def establish_connection(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print(self.client_socket.recv(2048).decode())

            while True:
                message = input(" -> ")

                if message.lower().strip() == 'bye':
                    break

                self.client_socket.send(message.encode())
                data = self.client_socket.recv(2048).decode()

                print('Received from server: ' + data)

            self.client_socket.close()

        except Exception as ex:
            print(ex)
            print("Failed to establish connection.")

        