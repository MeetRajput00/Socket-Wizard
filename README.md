
# Socket Wizard

Socket Wizard is a CLI tool developed using Python, designed specifically for educational purposes. It showcases various socket programming techniques by providing functionality to create a server and a client for a given host and port. As a work in progress, Socket Wizard aims to expand its feature set to include additional capabilities, such as a multi-threaded web server. The primary goal of the tool is to serve as a learning resource for individuals interested in understanding and implementing different aspects of socket programming.


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
- Mass IP/Host Scanner
- Web Login bruteforce tool (Threaded)
- SSH Login bruteforce tool (Threaded)
- FTP Login bruteforce tool (Threaded)

## Future updates
(This list is updated from https://github.com/kurogai/100-redteam-projects)
- FTP User footprint
- MYSQL User footprint
- Simple Google Bot for web scan
- Auto website comment bot
- Auto website message bot
- Web-scrapping using Regex


## Installation

To use Socket Wizard, first install all the requirements with pip

```bash
  pip install -r requirements.txt
```

## Usage/Examples

To create a Server
```
py SocketWizard.py server --port <port-number>
```
To create a Client
```
py SocketWizard.py client --host <host-name> --port <port-number>
```
To find your IP and hostname
```
py SocketWizard.py myIP
```
To do a port scan
```
py SocketWizard.py scan --target <target-ip> --ports <firstPort-lastPort>
```


## Contributing

Contributions are always welcome!

## NOTES

It is Only For Educational Purposes. Neither I Say Nor I Promote To Do Anything Illegal.

## Project Contributors
<a href="https://github.com/MeetRajput00/Socket-Wizard/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=MeetRajput00/Socket-Wizard" />
</a>


## Feedback

If you have any feedback, please reach out to us at rajputmeet10@gmail.com

    
## License

[MIT](https://choosealicense.com/licenses/mit/)




