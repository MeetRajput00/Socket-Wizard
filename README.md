
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
- Mass IP/Host Scanner

## Future updates
(This list is updated from https://github.com/kurogai/100-redteam-projects)
- Real-Time Data Streaming
- P2P File Sharing
- Multiplayer Game
- Remote Desktop Control
- Recursive Web Directory brute-forcer (Threaded peer recursion)
- Web Login bruteforce tool
- FTP Login bruteforce tool
- SSH Login bruteforce tool 
- FTP User footprint
- MYSQL User footprint
- Simple Google Bot for web scan
- Auto website comment bot
- Auto website message bot
- Web-scrapping using Regex
- Bot to collect information about someone using Google / Bing / Yahoo! 
- Simple SQLi tester
- Simple XSS tester
- Simple Wordpress brute-forcer
- SQLi database retriever
- Spam creator
- Payload for reverse shell
- Payload to capture screenshots
- Implement a Botnet
- Passive web scanner
- ARP poisoning tool
- Application that creates random shortcuts on screen
- Application to encrypt a file 
- Develop a Ransomware application
- Spam Email sender
- HTTP server for phishing
- Honeypot creator
- Application that connects to the Tor Network
- IRC Server
- Packet Capture tool
- Packet Data analysis
- Packet image analysis with OpenCV
- Develop a hexdump tool 
- Payload that moves the mouse cursor
- Vigenère Cipher
- Payload that starts automatically using Windows Regedit
- Payload that starts as a daemon
- Payload that retrieves browser information
- Link generator
- ASCII Name generator [ just for fun :) ]
- Full chat server with private messages, file and image transfer
- Simple firewall
- Gateway
- Powershell payload generator
- Bash payload generator
- Subdomain enumerator
- DNS Enumerator
- Your own interpreter
- Develop a Worm
- Server for DDOS
- Implement an IP Tracker
- BurpSuite extender
- Develop a Trojan
- Man In The Browser tool (kind of)
- Process monitor (Windows and Linux)
- Windows token privilege escalation tool
- Develop a code injection tool
- Develop a Worm with auto replication over email
- Simple Disassembler
- Server for DDoS with multi-staged operations and multi-threaded handling of clients
- Password hash cracker
- Direct code injection exploit
- Android daemon payload
- Browser exploitation tool
- Simple tool for Reverse Engineering
- Script for OS enumeration (after shell)
- RSA Payload generator
- Handshake capture
- Wifi monitor
- Buffer Overflow exploit
- Stack Overflow exploit
- Banner exploit
- ISS Exploit
- Wifi de-authentication attack (DoS) tool
- Badchar detector
- Firewall detector
- Exploitation Framework
- Botnet with SSH C&C and automatic server backup to prevent loss of control
- Windows enumeration tool
- Application information gathering (after shell)
- Recreate TCPDUMP
- Bluetooth exploit
- Windows Blue Screen Exploit
- Encoded exploit
- Antivirus evasion application
- Your own metasploit module



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




