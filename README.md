
# Ports

Ports is a CLI tool developed using Python, designed specifically for educational purposes. It showcases various socket programming techniques by providing functionality to create a server and a client for a given host and port. As a work in progress, Ports aims to expand its feature set to include additional capabilities, such as a multi-threaded web server. The primary goal of the tool is to serve as a learning resource for individuals interested in understanding and implementing different aspects of socket programming.


## Features

- Server/Client chat application
- Get IP/Host info
- Chatroom Update
- Port Scanner
- File Transfer Application
- TCP/UDP server client support
- Caesar Cipher and ROT13 encryption added
- Remote Code Execution
- OS Detection using TTL
- Web Directory Enumeration(Threaded)

## Future updates

- Real-Time Data Streaming
- P2P File Sharing
- Multiplayer Game
- Remote Desktop Control
- Mass IP/Host Scanner


## Installation

To use ports, first install all the requirements with pip

```bash
  pip install -r requirements.txt
```

## Usage/Examples

To create a Server
```
py port.py server --port <port-number>
```
To create a Client
```
py port.py client --host <host-name> --port <port-number>
```
To find your IP and hostname
```
py port.py myIP
```
To do a port scan
```
py port.py scan --target <target-ip> --ports <firstPort-lastPort>
```


## Contributing

Contributions are always welcome!


## Authors

- [@MeetRajput00](https://www.github.com/MeetRajput00)


## Feedback

If you have any feedback, please reach out to us at rajputmeet10@gmail.com

    
## License

[MIT](https://choosealicense.com/licenses/mit/)




