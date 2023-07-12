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
        git_pull("")

        # TODO : 해당 프로젝트의 파일을 전부 읽는다.
        found_files = search_files('', '')
        logger.debug(f"{Fore.GREEN} found_files: {found_files}")

        # 코드를 로드하고 주석을 추가할 파일을 선택합니다.
        filepath = './data/project/code-mentor/code-mentor/test-data/test-code.ts'
        with open(filepath, 'r') as file:
            code = file.read()
        openai.api_key = os.getenv('OPENAI_API_KEY')

        def get_comment_for_code(code):
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Please refactor comment this code :{code}\n#",
                temperature=0.5,
                max_tokens=2000,
            )
            return response.choices[0].text.strip()

        # 여기를 어떻게 처리 할 것인가.


        commented_code = get_comment_for_code(code)
        print(commented_code)
        # GPT-3에게 설명을 생성하도록 요청합니다.
