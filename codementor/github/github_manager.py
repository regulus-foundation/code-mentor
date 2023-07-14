import requests
import json
import os

def pull_request_github(to_branch, from_branch):

    token = os.getenv('GIT_HUB_TOKEN')
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    data = {
        'title': 'Your Pull Request Title',
        'head': from_branch,  # 병합하려는 브랜치 이름
        'base': to_branch,  # 기준이 되는 브랜치 이름
        'body': 'Description of the pull request',  # PR에 대한 설명
    }

    response = requests.post(
        'https://api.github.com/repos/regulus-foundation/code-mentor/pulls',
        headers=headers,
        data=json.dumps(data),
    )

    if response.status_code == 201:
        print('Pull request successfully created')
    else:
        print(f'Error: {response.status_code}')
        print(response.text)
    pass
