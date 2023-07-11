import time
from codementor.logs import logger
from codementor.git.git_manager import git_clone, git_checkout
from colorama import Fore, Style
import openai
import os



class Agent:

    def start_interaction_loop(self):

        # git_clone("", "")
        git_checkout("", "develop")


        # openai.api_key = os.getenv('OPENAI_API_KEY')
        # logger.debug(f"{Fore.GREEN} starting interaction loop")
        # chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
        #                                                messages=[{"role": "user", "content": "Hello world"}])
        #
        # logger.debug(f"{Fore.GREEN} chat_completion: {chat_completion}")
        # while True:
        #     logger.debug(f"{Fore.GREEN} logging test")
        #     time.sleep(1)
