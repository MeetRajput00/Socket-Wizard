import typer
import pyfiglet
from typing import Optional
from scripts.Sockets.Server import Server
from scripts.Sockets.Client import Client
from scripts.Network.Lookup.IP import IP
from scripts.Network.Scanner.PortScanner import PortScanner
from scripts.Discovery.WebDirectory import WebDirectoryBruteForcer
app = typer.Typer()

@app.command("server")
def start_server(port: Optional[int]=12345,connections: Optional[int]=5,broadcast: Optional[int]=0,udp: Optional[int]=0,encryption: Optional[str]='ROT13'):
    server=Server(port=port,connections=connections,broadcast=broadcast,udp=udp,encryption=encryption)
    server.start_server()

@app.command("client")
def start_client(host: Optional[str]='127.0.0.1', port: Optional[int]=12345,udp: Optional[int]=0,encryption: Optional[str]='ROT13'):
    client=Client(host=host, port=port,udp=udp,encryption=encryption)
    client.establish_connection()

@app.command("IP")
def get_client_info(target: Optional[str]='127.0.0.1'):
    ip=IP(target=target)
    print(f'IP \t \t \t \t Host ')
    ip_addresses = ip.get_ip_addresses()
    hostnames = ip.get_hostnames()

    for i, j in zip(ip_addresses, hostnames):
        print(f'{i} \t \t {j}')
@app.command('scan')
def scan_target(target:Optional[str]='127.0.0.1',ports:Optional[str]='1-65536',commonPorts:Optional[int]=0,threads:Optional[int]=5):
    port_scanner=PortScanner(target=target,ports=ports,common_ports=commonPorts,threads=threads)
    port_scanner.port_scanner()

@app.command('web-dir-enum')
def start_web_dir_enum(target:Optional[str]='127.0.0.1',threads:Optional[int]=5,filterCodes:Optional[str]='200,301',recursive:Optional[int]=0):
    web_dir_enum=WebDirectoryBruteForcer(target=target,threads=threads,filterCodes=filterCodes,recursive=recursive)
    web_dir_enum.brute()

if __name__ == "__main__":
    ascii_banner=pyfiglet.figlet_format("PORTS")
    print(ascii_banner)
    app()    