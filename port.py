import typer
import pyfiglet
from typing import Optional
from app.Sockets.Server import Server
from app.Sockets.Client import Client
from app.Network.Lookup.IP import IP
from app.Network.Scanner.PortScanner import PortScanner
app = typer.Typer()

@app.command("server")
def start_server(port: Optional[int]=12345,connections: Optional[int]=5,broadcast: Optional[int]=0,udp: Optional[int]=0):
    server=Server(port=port,connections=connections,broadcast=broadcast,udp=udp)
    server.start_server()

@app.command("client")
def start_client(host: Optional[str]='127.0.0.1', port: Optional[int]=12345,udp: Optional[int]=0):
    client=Client(host=host, port=port,udp=udp)
    client.establish_connection()

@app.command("myIP")
def get_client_info():
    ip=IP()
    print(f'IP: {ip.get_ip_address()}\t Host: {ip.get_hostname()}')

@app.command('scan')
def scan_target(target:Optional[str]='127.0.0.1',ports:Optional[str]='1-65536'):
    port_scanner=PortScanner(target=target,ports=ports)
    port_scanner.port_scanner()

if __name__ == "__main__":
    ascii_banner=pyfiglet.figlet_format("PORTS")
    print(ascii_banner)
    app()    