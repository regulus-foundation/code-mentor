import time

from codementor.alarm.telegram import request_telegram_alarm
from codementor.file.file_manager import search_files
from codementor.github.github_manager import pull_request_github
from codementor.logs import logger
from codementor.git.git_manager import git_clone, git_checkout, git_pull, git_merge_origin, git_commit, git_push, \
    git_checkout_new_branch, git_add_all, git_fetch_origin
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
    git_fetch_origin(code_project_dir, project_name, git_to_merge_branch)

    # how to solve git conflict

    # check already have branch
    git_checkout_new_branch(code_project_dir, git_from_merge_branch, project_name)
    # if not have branch. create new branch and push

    git_merge_origin(code_project_dir, git_to_merge_branch, project_name)


def call_openai_api_for_code_comment(code):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # openai.api_key = os.getenv("OPENAI_API_KEY")
    # print(openai.Model.list())

    content_value = f"Please meticulously transform the provided code into a well-structured markdown documentation suitable for a production release. Exclude any comments related to imports, but ensure the preservation of license and ESLint notes. Here's the code to be transformed:\n{code}"


    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": content_value}
        ]
    )

    commented_code = completion.choices[0].message.content

    print(f"docs: {commented_code}")

    return commented_code


def start_interaction_loop():
    logger.info(f"start_interaction_loop")
    git_hub_repo = os.getenv('GIT_HUB_REPO')
    code_project_dir = os.getenv('CODE_PROJECT_DIR')
    git_to_merge_branch = os.getenv('GIT_TO_MERGE_BRANCH')
    git_from_merge_branch = os.getenv('GIT_FROM_MERGE_BRANCH')

    while True:

        project_name = git_hub_repo.split('/')[-1].split('.')[0]

        found_files = search_files(code_project_dir)
        logger.debug(f"{Fore.GREEN} found_files: {found_files}")

        for filepath in found_files:
            with open(filepath, 'r') as file:
                code = file.read()

            print(f"code: {code}")
            docs_code = call_openai_api_for_code_comment(code)
            print(f"docs_code: {docs_code}")
            docsPath = filepath.replace('.ts', '.md')

            # code-mentor:docs 를 삭제합니다.
            with open(filepath, 'w') as file:
                file.write(code.replace('code-mentor:docs', ''))

            # 파일을 쓰기 모드(w)로 열고 md 파일을 씁니다.
            with open(docsPath, 'w') as file:
                file.write(docs_code)

        if not found_files:
            logger.info(f"not found files")
        else:
            logger.info(f"found files")
            # git_add_all(code_project_dir, project_name)
            #
            # git_commit(code_project_dir, "add comment", project_name)
            # git_push(code_project_dir, project_name, git_from_merge_branch)
            # pull_request_github(git_to_merge_branch, git_from_merge_branch)
            # request_telegram_alarm()
        time.sleep(60)


class Agent:
    pass
