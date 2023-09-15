import subprocess
import os

from codementor.logs import logger


def git_clone(repo_url, save_to_path, project_name):
    try:

        # git clone 명령어 실행
        if not os.path.exists(save_to_path):
            os.makedirs(save_to_path)

        if os.path.exists(save_to_path + '/' + project_name):
            logger.info(f"Already exists {project_name}")
            return

        cmd = ["git", "clone", repo_url]
        subprocess.run(cmd, cwd=save_to_path, check=True)
        logger.info(f"Successfully cloned {repo_url}")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while cloning the repo: {repo_url}")
        logger.info(f"Error message: {e}")
        raise e


def git_checkout(save_to_path, branch_name, project_name):
    try:
        # git clone 명령어 실행
        cmd = ["git", "checkout", branch_name]
        subprocess.run(cmd, cwd=save_to_path + "/" + project_name, check=True)
        logger.info(f"Successfully checkout {branch_name}")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while checkout the branch: {branch_name}")
        logger.info(f"Error message: {e}")
        raise e


def git_checkout_new_branch(save_to_path, branch_name, project_name):
    try:
        # git clone 명령어 실행
        cmd = ["git", "checkout", "-b", branch_name]
        subprocess.run(cmd, cwd=save_to_path + "/" + project_name, check=True)
        logger.info(f"Successfully checkout {branch_name}")

    except subprocess.CalledProcessError as e:
        logger.info(f"Already have branch: {e}")


def git_merge_origin(save_to_path, target_branch_name, project_name):
    try:

        # git clone 명령어 실행
        cmd = ["git", "merge", f"origin/{target_branch_name}"]
        subprocess.run(cmd, cwd=save_to_path + "/" + project_name, check=True)
        logger.info(f"Successfully merge {target_branch_name}")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while merge the target_branch_name: {target_branch_name}")
        logger.info(f"Error message: {e}")
        raise e


def git_pull(save_to_path, project_name):
    try:
        # git clone 명령어 실행
        cmd = ["git", "pull"]
        subprocess.run(cmd, cwd=save_to_path + "/" + project_name, check=True)
        logger.info(f"Successfully pull")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while pull")
        logger.info(f"Error message: {e}")
        raise e


def git_fetch_origin(save_to_path, project_name, branch_name):
    try:
        # git clone 명령어 실행
        cmd = ["git", "fetch", "origin", branch_name]
        subprocess.run(cmd, cwd=save_to_path + "/" + project_name, check=True)
        logger.info(f"Successfully fetch")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while fetch")
        logger.info(f"Error message: {e}")
        raise e


def git_add_all(save_to_path, project_name):
    try:
        # git clone 명령어 실행
        cmd = ["git", "add", "*"]
        subprocess.run(cmd, cwd=save_to_path + "/" + project_name, check=True)
        logger.info(f"Successfully git add all")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while git add")
        logger.info(f"Error message: {e}")
        raise e


def git_commit(save_to_path, commit_message, project_name):
    try:
        # git clone 명령어 실행
        cmd = ["git", "commit", "-m", commit_message]
        subprocess.run(cmd, cwd=save_to_path + "/" + project_name, check=True)
        logger.info(f"Successfully commit")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while commit")


def git_push(save_to_path, project_name, branch_name):
    try:
        # git push 명령어 실행
        cmd = ["git", "push", "--set-upstream", "origin", branch_name]
        subprocess.run(cmd, cwd=save_to_path + "/" + project_name, check=True)
        logger.info(f"Successfully push")

    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred while push")
        logger.info(f"Error message: {e}")
        raise e
