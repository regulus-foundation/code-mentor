import subprocess
import os

from codementor.logs import logger


def git_clone(repo_url, save_to_path):
    try:

        if not os.path.exists(save_to_path):
            os.makedirs(save_to_path)

        cmd = ["git", "clone", repo_url]
        subprocess.run(cmd, cwd=save_to_path, check=True)
        logger.info(f"Successfully cloned {repo_url}")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while cloning the repo: {repo_url}")
        logger.info(f"Error message: {e}")


def git_checkout(save_to_path, branch_name):
    try:
        # git clone 명령어 실행
        cmd = ["git", "checkout", branch_name]
        subprocess.run(cmd, cwd=save_to_path, check=True)
        logger.info(f"Successfully checkout {branch_name}")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while checkout the branch: {branch_name}")
        logger.info(f"Error message: {e}")


def git_merge(save_to_path, target_branch_name):
    try:

        # git clone 명령어 실행
        cmd = ["git", "merge", target_branch_name]
        subprocess.run(cmd, cwd=save_to_path, check=True)
        logger.info(f"Successfully checkout {target_branch_name}")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while merge the target_branch_name: {target_branch_name}")
        logger.info(f"Error message: {e}")


def git_pull(save_to_path):
    try:
        # git clone 명령어 실행
        cmd = ["git", "pull"]
        subprocess.run(cmd, cwd=save_to_path, check=True)
        logger.info(f"Successfully pull")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while pull")
        logger.info(f"Error message: {e}")


def git_commit(save_to_path, commit_message):
    try:
        # git clone 명령어 실행
        cmd = ["git", "commit", "-m", commit_message]
        subprocess.run(cmd, cwd=save_to_path, check=True)
        logger.info(f"Successfully commit")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while commit")
        logger.info(f"Error message: {e}")


def git_push(save_to_path):
    try:
        # git push 명령어 실행
        cmd = ["git", "push"]
        subprocess.run(cmd, cwd=save_to_path, check=True)
        logger.info(f"Successfully push")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while push")
        logger.info(f"Error message: {e}")
