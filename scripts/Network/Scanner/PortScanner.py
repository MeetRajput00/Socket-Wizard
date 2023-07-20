import socket
from datetime import datetime
import subprocess
import re
from concurrent.futures import ThreadPoolExecutor
import json
class PortScanner:
    def __init__(self,target:str,ports:str,common_ports:int,threads:int) -> None:
        self.target=socket.gethostbyname(target)
        self.threads=threads
        ports_range=ports.split('-')
        if common_ports==0:
            self.ports=list(range(int(ports_range[0]), int(ports_range[1]) + 1))
        else:
            self.ports=json.load(open('./temp_files/common_open_ports.json'))
    def scan_port(self,port:int):
        try:
            s = socket.socket()
            response=s.connect_ex((self.target, int(port)))
            if response==0:
                print(str(port) + " \t open "+f'\t {self.service(port)}')
            s.close()
        except Exception as e:
            pass
    def port_scanner(self):
        print("[+] Target: " + self.target)
        start_time=datetime.now()
        print(f'[+] Scanning started at {start_time}\n')
        print('Port \t State \t Service')
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self.scan_port, self.ports)
        stop_time=datetime.now()
        print(f'\n[+] OS detected: {self.get_os_from_ttl(self.send_icmp_packet(self.target))}')
        print(f'[+] Scanning finished at {stop_time}')
        print(f'[+] Scanning duration: {stop_time-start_time}')
    
    def service(self,port):
        service_list = json.load(open('./temp_files/common_ports_services.json'))
        try:
            return service_list[str(port)]
        except:
            return "unknown"
    
    def send_icmp_packet(self,destination_address:str):
        result = subprocess.run(['ping', destination_address], capture_output=True, text=True)
        output = result.stdout

        # Extract the TTL value using regular expression
        ttl_match = re.search(r'TTL=(\d+)', output)
        if ttl_match:
            ttl = int(ttl_match.group(1))
            return ttl

        return None
    
    def get_os_from_ttl(self,ttl:int):
        os_dict = json.load(open('./temp_files/os_detection_ports.json'))
        
        os = os_dict.get(ttl)
        return os


