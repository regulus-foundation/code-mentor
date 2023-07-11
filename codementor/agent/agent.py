import time

from codementor.file.file_manager import search_files
from codementor.logs import logger
from codementor.git.git_manager import git_clone, git_checkout, git_pull
from colorama import Fore, Style
import openai
import os



class Agent:

    def start_interaction_loop(self):

        # git_clone("", "")
        # git_checkout("", "develop")
        # git_pull("")

        # TODO : 해당 프로젝트의 파일을 전부 읽는다.
        found_files = search_files('', '')
        logger.debug(f"{Fore.GREEN} found_files: {found_files}")
        # TODO : 특별한 Prompt 가 있는지 체크 한다.
        # TODO : 특별한 Prompt 가 있으면 ChatGpt 에게 해당 내용은 요청 한다.
        # TODO : Branch 를 변경 한다.
        # TODO : ChatGpt 에게 요청한 내용을 받는다.
        # TODO : 해당 브랜치에 파일을 덮어 쓴다.
        # TODO : Git Push 한다.
        # TODO : GitHub 에 Merge Request 를 요청 한다.
        # TODO : 해당 파일을 Marking 한다.




        # openai.api_key = os.getenv('OPENAI_API_KEY')
        # logger.debug(f"{Fore.GREEN} starting interaction loop")
        # chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
        #                                                messages=[{"role": "user", "content": "Hello world"}])
        #
        # logger.debug(f"{Fore.GREEN} chat_completion: {chat_completion}")
        # while True:
        #     logger.debug(f"{Fore.GREEN} logging test")
        #     time.sleep(1)
