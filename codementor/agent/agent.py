import time

from codementor.alarm.telegram import request_telegram_alarm
from codementor.file.file_manager import search_files
from codementor.github.github_manager import pull_request_github
from codementor.logs import logger
from codementor.git.git_manager import git_clone, git_checkout, git_pull, git_merge, git_commit, git_push, \
    git_checkout_new_branch, git_add_all, git_fetch
from colorama import Fore

import os
import openai


def initialize_git_setting():

    logger.info(f"initialize_git_setting")

    git_hub_repo = os.getenv('GIT_HUB_REPO')
    git_to_merge_branch = os.getenv('GIT_TO_MERGE_BRANCH')
    git_from_merge_branch = os.getenv('GIT_FROM_MERGE_BRANCH')

    code_project_dir = os.getenv('CODE_PROJECT_DIR')
    project_name = git_hub_repo.split('/')[-1].split('.')[0]

    git_clone(git_hub_repo, code_project_dir, project_name)

    # git_checkout(code_project_dir, git_to_merge_branch, project_name)
    # git pull
    git_fetch(code_project_dir, project_name)

    # how to solve git conflict

    # check already have branch
    git_checkout_new_branch(code_project_dir, git_from_merge_branch, project_name)
    # if not have branch. create new branch and push

    git_merge(code_project_dir, 'origin/' + git_to_merge_branch, project_name)


def call_openai_api_for_code_comment(code):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Please refactor comment this code:{code}\n#",
        temperature=0.5,
        max_tokens=2000,
    )

    commented_code = response.choices[0].text.strip()
    commented_code = commented_code.replace('Refactored\n', '')
    commented_code = commented_code.replace('Refactored Code\n', '')

    return commented_code


def start_interaction_loop():
    logger.info(f"start_interaction_loop")

    while True:

        git_hub_repo = os.getenv('GIT_HUB_REPO')
        code_project_dir = os.getenv('CODE_PROJECT_DIR')
        git_to_merge_branch = os.getenv('GIT_TO_MERGE_BRANCH')
        git_from_merge_branch = os.getenv('GIT_FROM_MERGE_BRANCH')

        project_name = git_hub_repo.split('/')[-1].split('.')[0]

        found_files = search_files(code_project_dir)
        logger.debug(f"{Fore.GREEN} found_files: {found_files}")

        for filepath in found_files:
            with open(filepath, 'r') as file:
                code = file.read()

            import_lines = [line for line in code.splitlines() if line.strip().startswith('import')]
            print(f"{Fore.GREEN} import_lines: {import_lines}")
            commented_code = call_openai_api_for_code_comment(code)

            # import 문장을 commented_code 앞에 다시 추가 합니다.
            commented_code = "\n".join(import_lines) + "\n" + commented_code

            # 파일을 쓰기 모드(w)로 열고 코멘트가 포함된 코드를 저장합니다.
            with open(filepath, 'w') as file:
                file.write(commented_code)

        if found_files is None:
            logger.info(f"not found files")
        else:
            logger.info(f"found files")
            git_add_all(code_project_dir, project_name)
            #
            git_commit(code_project_dir, "add comment", project_name)
            git_push(code_project_dir, project_name, git_from_merge_branch)
            pull_request_github(git_to_merge_branch, git_from_merge_branch)
            # request_telegram_alarm()
        time.sleep(60)


class Agent:
    pass
