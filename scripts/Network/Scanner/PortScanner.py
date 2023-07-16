import socket
from datetime import datetime

class PortScanner:
    def __init__(self,target:str,ports:str) -> None:
        self.target=target
        ports_range=ports.split('-')
        self.ports=list(range(int(ports_range[0]), int(ports_range[1]) + 1))

    def port_scanner(self):
        print("[+] Target: " + self.target)
        start_time=datetime.now()
        print(f'[+] Scanning started at {start_time}\n')
        for port in self.ports:
            try:
                s = socket.socket()
                response=s.connect_ex((self.target, int(port)))
                if response==0:
                    print("[+] Port " + str(port) + ": open ")
                s.close()
            except Exception as e:
                pass
        stop_time=datetime.now()
        print(f'[+] Scanning finished at {stop_time}')
        print(f'[+] Scanning duaring: {stop_time-start_time}')