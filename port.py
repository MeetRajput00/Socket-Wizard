import typer
from typing import Optional
from app.Sockets.Server import Server
from app.Sockets.Client import Client
from app.Network.IP import IP

app = typer.Typer()

@app.command("server")
def start_server(port: Optional[int]=12345,connections: Optional[int]=5,broadcast: Optional[int]=0):
    server=Server(port=port,connections=connections,broadcast=broadcast)
    server.start_server()

@app.command("client")
def start_client(host: Optional[str]='127.0.0.1', port: Optional[int]=12345):
    client=Client(host=host, port=port)
    client.establish_connection()

@app.command("myIP")
def get_client_info():
    ip=IP()
    print(f'IP: {ip.get_ip_address()}\t Host: {ip.get_hostname()}')


if __name__ == "__main__":
    app()    