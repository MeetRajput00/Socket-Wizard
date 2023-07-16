import socket
import threading
import subprocess
from tqdm import tqdm
import os
from scripts.Encryption.Encryption import ROT13Cipher, CaesarCipher

class Server:
    def __init__(self, port: int, connections: int,broadcast: int,udp: int,encryption: str) -> None:
        self.host = '127.0.0.1'
        self.port = port
        if encryption=='caesar-cipher':
            self.encryption=CaesarCipher(shift=25)
        else:
            self.encryption=ROT13Cipher()
        if udp==1:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.maximum_connections = connections
        self.is_broadcast_enabled=broadcast
        self.list_of_clients = []
        self.print_lock = threading.Lock()

    def client_thread(self, conn: socket.socket, addr: tuple) -> None:
        while True:
            try:
                message = self.encryption.decrypt(conn.recv(2048).decode())
                if message=='rce-mode':
                    response=input("Client is requesting file upload.(y/n)-> ")
                    if response=='y':
                        with self.print_lock:
                            conn.send(self.encryption.encrypt('y').encode())
                            command_str = self.encryption.decrypt(conn.recv(SIZE).decode(FORMAT))
                            command_list=command_str.split('>')
                            response_obj=subprocess.check_output(command_list)
                            conn.send(self.encryption.encrypt(response_obj).encode())
                    elif response=='n':
                        conn.send(self.encryption.encrypt('n').encode())
                    else:
                        break
                elif message=='ft-mode-upload':
                    response=input("Client is requesting file upload.(y/n)-> ")
                    if response=='y':
                        with self.print_lock:
                            conn.send(self.encryption.encrypt('y').encode())
                            SIZE = 1024
                            FORMAT = "utf-8"
                            data = self.encryption.decrypt(conn.recv(SIZE).decode(FORMAT))
                            item = data.split("_")
                            FILENAME = item[0]
                            FILESIZE = int(item[1])
                            conn.send(self.encryption.encrypt(f'{FILENAME}_{FILESIZE}').encode(FORMAT))
                            bar = tqdm(total=FILESIZE,initial=0,desc=f"Receiving {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)
                            with open(f"recv_{FILENAME}", "wb") as f:
                                while True:
                                    data = conn.recv(SIZE).decode(FORMAT)               
                                    if data=='\eof':
                                        break
                                    f.write(data.encode(FORMAT))
                        
                                    bar.update(len(data))
                            
                            print("File received.")
                    elif response=='n':
                        conn.send(self.encryption.encrypt('n').encode())
                    else:
                        break
                elif message=='ft-mode-download':
                    response=input("Client is requesting file download.(y/n)-> ")
                    if response=='y':
                        with self.print_lock:
                            conn.send(self.encryption.encrypt('y').encode())
                            SIZE = 1024
                            FORMAT = "utf-8"
                            FILENAME = self.encryption.decrypt(conn.recv(SIZE).decode(FORMAT))
                            FILESIZE = os.path.getsize(FILENAME)
                            conn.send(self.encryption.encrypt(f'{FILENAME}_{FILESIZE}').encode(FORMAT))
                            bar = tqdm(total=FILESIZE,initial=0,desc=f"Receiving {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)
                            with open(FILENAME, "rb") as f:
                                while True:
                                    data = f.read(SIZE)
                        
                                    if not data:
                                        conn.send(self.encryption.encrypt('\eof').encode(FORMAT))
                                        break
                        
                                    conn.send(data)
                        
                                    bar.update(len(data))
                            print('File sent.')
                    elif response=='n':
                        conn.send(self.encryption.encrypt('n').encode())
                    else:
                        break
                elif message:
                    print("<" + addr[0] + "> " + message)
                    if(self.is_broadcast_enabled==1):
                        self.broadcast(message, conn)
                    message_to_send = input("->")
                    conn.send(self.encryption.encrypt(message_to_send).encode())
                    if(self.is_broadcast_enabled==1):
                        self.broadcast(message_to_send,conn)

                else:
                    self.remove(conn)

            except Exception as ex:
                print(ex)
                break

    def broadcast(self, message: str, connection: socket.socket) -> None:
        with self.print_lock:
            for client in self.list_of_clients:
                if client != connection:
                    try:
                        client.send(message.encode())
                    except Exception:
                        client.close()
                        self.remove(client)

    def remove(self, connection: socket.socket) -> None:
        if connection in self.list_of_clients:
            self.list_of_clients.remove(connection)

    def start_server(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(self.maximum_connections)
            print(f"Host: {self.host}\t Port: {self.port}\t Maximum Connection: {self.maximum_connections}")
            print("Server started.")
            while True:
                conn, addr = self.server_socket.accept()
                self.list_of_clients.append(conn)
                print(addr[0] + " connected")
                threading.Thread(target=self.client_thread, args=(conn, addr)).start()

        except Exception as ex:
            print(ex)
            print("Failed to establish connection.")

        finally:
            for conn in self.list_of_clients:
                conn.close()

            self.server_socket.close()

