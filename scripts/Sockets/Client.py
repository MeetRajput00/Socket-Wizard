import socket
import os
from tqdm import tqdm

class Client:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def establish_connection(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print("----for file transfer: send ft-mode to server----")
            print(self.client_socket.recv(2048).decode())

            while True:
                message = input(" -> ")

                self.client_socket.send(message.encode())
                data = self.client_socket.recv(2048).decode()
                if message=='ft-mode':
                    if data =='y':
                        SIZE = 1024
                        FORMAT = "utf-8"
                        FILENAME=input("Enter file path->")
                        FILESIZE = os.path.getsize(FILENAME)

                        data = f"{FILENAME}_{FILESIZE}"
                        self.client_socket.send(data.encode(FORMAT))
                        msg = self.client_socket.recv(SIZE).decode(FORMAT)
                        print(f"SERVER: {msg}")

                        bar = tqdm(total=FILESIZE,initial=0, desc=f"Sending {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)
 
                        with open(FILENAME, "rb") as f:
                            while True:
                                data = f.read(SIZE)
                    
                                if not data:
                                    self.client_socket.send('\eof'.encode(FORMAT))
                                    break
                    
                                self.client_socket.send(data)
                    
                                bar.update(len(data))
                        print('File sent.')
                    else:
                        print(">ft-mode request denied by server.")
                else:
                    print('Received from server: ' + data)

            self.client_socket.close()

        except Exception as ex:
            print(ex)
            print("Failed to establish connection.")

        