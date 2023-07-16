import socket
import os
from tqdm import tqdm
from scripts.Encryption.Encryption import ROT13Cipher, CaesarCipher

class Client:
    def __init__(self, host: str, port: int,udp: int,encryption: str) -> None:
        self.host = host
        self.port = port
        if encryption=='caesar-cipher':
            self.encryption=CaesarCipher(shift=25)
        else:
            self.encryption=ROT13Cipher()
        if udp==1:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def establish_connection(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print("----for file transfer: send ft-mode to server----")
            print(f'[+]{self.host} connected.')

            while True:
                message = input(" -> ")

                self.client_socket.send(self.encryption.encrypt(message).encode())
                data = self.encryption.decrypt(self.client_socket.recv(2048).decode())
                if message=='ft-mode-upload':
                    if data =='y':
                        SIZE = 1024
                        FORMAT = "utf-8"
                        FILENAME=input("Enter file path->")
                        FILESIZE = os.path.getsize(FILENAME)

                        data = f"{FILENAME}_{FILESIZE}"
                        self.client_socket.send(self.encryption.encrypt(data).encode(FORMAT))
                        msg = self.encryption.decrypt(self.client_socket.recv(SIZE).decode(FORMAT))
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
                            print(">ft-mode-download request denied by server.")
                elif message=='ft-mode-download':
                    if data =='y':
                        SIZE = 1024
                        FORMAT = "utf-8"
                        FILENAME=input("Enter file path->")

                        data = f"{FILENAME}"
                        self.client_socket.send(self.encryption.encrypt(data).encode(FORMAT))
                        msg = self.encryption.decrypt(self.client_socket.recv(SIZE).decode(FORMAT))
                        print(f"SERVER: {msg}")

                        bar = tqdm(total=FILESIZE,initial=0, desc=f"Sending {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

                        with open(f"recv_{FILENAME}", "wb") as f:
                            while True:
                                data = self.client_socket.recv(SIZE).decode(FORMAT)               
                                if data=='\eof':
                                    break
                                f.write(data.encode(FORMAT))
                    
                                bar.update(len(data))
                        
                        print("File received.")
                    else:
                        print(">ft-mode-download request denied by server.")
                else:
                    print('Received from server: ' + data)

            self.client_socket.close()

        except Exception as ex:
            print(ex)
            print("Failed to establish connection.")

        