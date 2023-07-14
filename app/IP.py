import socket

class IP:
    def __init__(self) -> None:
        self.temp_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def get_ip_address(self):
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception as ex:
            print(ex)
            return None

    def get_hostname(self)->None:
        try:
            return socket.gethostname()
        except Exception as ex:
            print(ex)
            return None