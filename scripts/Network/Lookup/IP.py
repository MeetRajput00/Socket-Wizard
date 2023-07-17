import socket
import ipaddress

class IP:
    def __init__(self, target: str) -> None:
        if '-' in target:
            start, end = target.split('-')
            self.targets = self.generate_ip_range(start.strip(), end.strip())
        else:
            self.targets = [socket.gethostbyname(target.strip())]

        self.temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def generate_ip_range(self, start: str, end: str) -> list:
        subnets=start.split('.')
        network_id = subnets[0]+'.'+subnets[1]+'.'+subnets[2]+'.'

        hosts= [host for host in range(int(subnets[3]),int(end)+1)]

        return [network_id+str(ip) for ip in hosts]


    def get_ip_addresses(self):
        return self.targets

    def get_hostnames(self) -> None:
        hostnames = []

        for target in self.targets:
            try:
                out = socket.gethostbyaddr(target)
                hostnames.append(out[0])
            except socket.herror:
                print(f"Hostname not found for the IP address: {target}")
            except Exception as ex:
                hostnames.append("N/A")

        return hostnames
