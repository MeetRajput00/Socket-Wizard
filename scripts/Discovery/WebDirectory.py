import requests
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import socket
import sys

class WebDirectoryBruteForcer:
    def __init__(self,target:str,threads:int,filterCodes:str) -> None:
        self.target=target
        self.threads=threads
        self.filter_codes=[]
        for codes in filterCodes.split(','):
            self.filter_codes.append(codes)
        self.dir_enum=[]
        with open(r'.\\temp_files\\directory-enum-list.txt','r') as fl:
            while True:
                data=fl.readline()
                if not data:
                    break
                self.dir_enum.append(data)
            

    def get_status_code(self,word:str):
        try:
            url2='https://'+self.target+"/"+word.strip()
            r=requests.get(url2)
            if str(r.status_code) in self.match:
                print(f"/{word.strip():<40}  [ Status: {r.status_code}  Length:{len(r.content)} ]")
        except KeyboardInterrupt:
            print("\nReceived Keyboard Interrupt  , Terminating threads\n")
            sys.exit()
        except Exception as e:
            print(f"\nAn error Occurred : {e}\n")
            sys.exit()
    def brute(self):
        print("[+] Target: " + self.target)
        print("[+] Filter Status Codes: ",end='')
        for codes in self.match:
            print(codes,end=',')
        start_time=datetime.now()
        print(f'[+] Directory enumeration started at {start_time}\n')
        with ThreadPoolExecutor(self.threads) as executor:
            executor.map(self.get_status_code,self.dir_enum)
        stop_time=datetime.now()
        print(f'[+] Directory enumeration finished at {stop_time}')
        print(f'[+] Total duration: {stop_time-start_time}')
