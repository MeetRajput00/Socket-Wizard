import socket

class Client:
    def __init__(self,host:str,port:int) -> None:
        self.host=host
        self.port=port
        self.client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def establish_connection(self):
        try:
            self.client_socket.connect((self.host, self.port))
            message = input(" -> ") 

            while message.lower().strip() != 'bye':
                self.client_socket.send(message.encode())
                data = self.client_socket.recv(1024).decode()

                print('Received from server: ' + data)

                message = input(" -> ") 

            self.client_socket.close() 
        except Exception as ex:
            print(ex)
            print("Failed to establish connection.")
        


if __name__ == '__main__':
    client=Client(host='127.0.0.1',port=8089)
    client.establish_connection()