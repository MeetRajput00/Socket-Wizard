import socket
import threading
import http.server
class ProxyServer:
    def __init__(self,port):
        self.host = '127.0.0.1'
        self.port = port

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)

        print(f"Proxy server started on {self.host}:{self.port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

            threading.Thread(target=self.handle_request, args=(server_socket,client_socket)).start()

    def handle_request(self,server_socket:socket.socket,client_socket:socket.socket):
        request_data = client_socket.recv(4096).decode()
        
         # Parse the request using http.server
        request = http.server.BaseHTTPRequestHandler(
            socket.socket(),
            client_address=('localhost', 0),
            server=socket.socket(),
        )
        request.rfile = http.server.BytesIO(request_data)
        request.parse_request()

        headers = request.headers

        host_header = headers.get('Host')
        if host_header:
            destination_host, _, destination_port = host_header.partition(':')
            destination_port = int(destination_port) if destination_port else 80
        else:
            raise Exception("Invalid request.")

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((destination_host, destination_port))
        server_socket.send(request_data.encode())


        response_data = server_socket.recv(4096).decode()

        client_socket.send(response_data.encode())

        server_socket.close()
        client_socket.close()

