import typer
import pyfiglet
from typing import Optional
from scripts.Sockets.Server import Server
from scripts.Sockets.Client import Client
from scripts.Network.Lookup.IP import IP
from scripts.Network.Scanner.PortScanner import PortScanner

app = typer.Typer()

@app.command("server")
def start_server(port: Optional[int]=12345,connections: Optional[int]=5,broadcast: Optional[int]=0,udp: Optional[int]=0,encryption: Optional[str]='ROT13'):
    server=Server(port=port,connections=connections,broadcast=broadcast,udp=udp,encryption=encryption)
    server.start_server()

@app.command("client")
def start_client(host: Optional[str]='127.0.0.1', port: Optional[int]=12345,udp: Optional[int]=0,encryption: Optional[str]='ROT13'):
    client=Client(host=host, port=port,udp=udp,encryption=encryption)
    client.establish_connection()

@app.command("myIP")
def get_client_info():
    ip=IP()
    print(f'IP: {ip.get_ip_address()}\t Host: {ip.get_hostname()}')

@app.command('scan')
def scan_target(target:Optional[str]='127.0.0.1',ports:Optional[str]='1-65536',commonPorts:Optional[int]=0):
    port_scanner=PortScanner(target=target,ports=ports,common_ports=commonPorts)
    port_scanner.port_scanner()

if __name__ == "__main__":
    ascii_banner=pyfiglet.figlet_format("PORTS")
    print(ascii_banner)
    app()    