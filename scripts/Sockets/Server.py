import socket
import threading
from tqdm import tqdm
import os

class Server:
    def __init__(self, port: int, connections: int,broadcast: int,udp: int) -> None:
        self.host = '127.0.0.1'
        self.port = port
        if udp==1:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.maximum_connections = connections
        self.is_broadcast_enabled=broadcast
        self.list_of_clients = []
        self.print_lock = threading.Lock()

    def client_thread(self, conn: socket.socket, addr: tuple) -> None:
        conn.send("Welcome to this chatroom!".encode())

        while True:
            try:
                message = conn.recv(2048).decode()
                if message=='ft-mode-upload':
                    response=input("Client is requesting file upload.(y/n)-> ")
                    if response=='y':
                        with self.print_lock:
                            conn.send('y'.encode())
                            SIZE = 1024
                            FORMAT = "utf-8"
                            data = conn.recv(SIZE).decode(FORMAT)
                            item = data.split("_")
                            FILENAME = item[0]
                            FILESIZE = int(item[1])
                            conn.send(f'{FILENAME}_{FILESIZE}'.encode(FORMAT))
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
                        conn.send('n'.encode())
                    else:
                        break
                elif message=='ft-mode-download':
                    response=input("Client is requesting file download.(y/n)-> ")
                    if response=='y':
                        with self.print_lock:
                            conn.send('y'.encode())
                            SIZE = 1024
                            FORMAT = "utf-8"
                            FILENAME = conn.recv(SIZE).decode(FORMAT)
                            FILESIZE = os.path.getsize(FILENAME)
                            conn.send(f'{FILENAME}_{FILESIZE}'.encode(FORMAT))
                            bar = tqdm(total=FILESIZE,initial=0,desc=f"Receiving {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)
                            with open(FILENAME, "rb") as f:
                                while True:
                                    data = f.read(SIZE)
                        
                                    if not data:
                                        conn.send('\eof'.encode(FORMAT))
                                        break
                        
                                    conn.send(data)
                        
                                    bar.update(len(data))
                            print('File sent.')
                    elif response=='n':
                        conn.send('n'.encode())
                    else:
                        break
                elif message:
                    print("<" + addr[0] + "> " + message)
                    if(self.is_broadcast_enabled==1):
                        self.broadcast(message, conn)
                    message_to_send = input("->")
                    conn.send(message_to_send.encode())
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

