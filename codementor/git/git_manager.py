import subprocess
import os

from codementor.logs import logger


def git_clone(repo_url, save_to_path):
    repo_url = "https://github.com/regulus-foundation/code-mentor.git"  # 복제하려는 저장소 주소를 지정합니다.
    save_to_path = "./data/project/code-mentor"  # 저장할 디렉토리의 경로를 지정합니다.

    try:
        # 저장할 디렉토리가 없으면 생성
        if not os.path.exists(save_to_path):
            os.makedirs(save_to_path)

        # git clone 명령어 실행
        cmd = ["git", "clone", repo_url]
        subprocess.run(cmd, cwd=save_to_path, check=True)
        logger.info(f"Successfully cloned {repo_url}")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while cloning the repo: {repo_url}")
        logger.info(f"Error message: {e}")


def git_checkout(save_to_path, branch_name):

    save_to_path = "./data/project/code-mentor"  # 저장할 디렉토리의 경로를 지정합니다.
    try:

        # git clone 명령어 실행
        cmd = ["git", "checkout", branch_name]
        subprocess.run(cmd, cwd=save_to_path, check=True)
        logger.info(f"Successfully checkout {branch_name}")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while checkout the branch: {branch_name}")
        logger.info(f"Error message: {e}")
