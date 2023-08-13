import time
import random
class RedditBot:
    def __init__(self,username:str,password:str) -> None:
        self.login(username=username, password=password)
        self.comment_list=self.fetch_files('./temp_files/ig_comment_list.txt')

    def fetch_files(self,file_path):
        return [item.replace("\n", "") for item in open(file_path).readlines()]
    
    def login(self, username, password):
        pass
    
    def auto_comment(self):
        target_username=input('Enter the target: ')
        num_comments=int(input("Enter no. of comments: "))
        media_ids = self.bot.get_user_medias(target_username, filtration=None)
        for media_id in media_ids[:num_comments]:
            comment = random.choice(self.comment_list)
            self.bot.comment(media_id, comment)
            time.sleep(10)  # Add a delay to avoid aggressive behavior


    def interactWithSomeone(self):
        comments=self.fetch_files('./temp_files/ig_comment_list.txt')
        user=input("Enter the username: ")
        self.session.set_comments(comments)
        self.session.set_do_comment(enabled=True, percentage=100)
        self.session.set_do_like(True, percentage=70)
        self.session.interact_by_users(user, amount=20, randomize=True, media='Photo')

if __name__=='__main__':
    


    





