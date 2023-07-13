import socket

class Server:
    def __init__(self,port:int) -> None:
        self.host='127.0.0.1'
        self.port=port
        self.server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def start_server(self):
        try:
            self.server_socket.bind((self.host, self.port)) 
            self.server_socket.listen(5)
            print("Server started.")
            while True:
                conn, address = self.server_socket.accept() 
                print("Connection from: " + str(address))
                data = conn.recv(1024).decode()
                if not data:
                    break
                print("from connected user: " + str(data))
                data = input(' -> ')
                conn.send(data.encode()) 

            conn.close() 
        except Exception as ex:
            print(ex)
            print("Failed to establish connection.")
         


if __name__ == '__main__':
    server=Server(port=8089)
    server.start_server()