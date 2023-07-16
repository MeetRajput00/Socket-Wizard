import socket

class PortScanner:
    def __init__(self,target:str,ports:str) -> None:
        self.target=target
        ports_range=ports.split('-')
        self.ports=list(range(int(ports_range[0]), int(ports_range[1]) + 1))

    def port_scanner(self):
        for port in self.ports:
            try:
                print("[+] Connecting to: " + self.target + " port:" + str(port))
                s = socket.socket()
                s.connect((self.target, int(port)))
                s.send('not_imp'.encode())
                banner = s.recv(1024).decode()
                if banner:
                    print("[+] Port " + str(port) + " open [+] \n" + banner)
                    s.close()
            except Exception as e:
                pass