import requests
import json
import os


# feature/regulus_test
# feature/code-mentor-test
def pull_request_github(to_branch, from_branch):
    token = os.getenv('GIT_HUB_TOKEN')
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    print(f'to_branch: {to_branch}')
    print(f'from_branch: {from_branch}')

    data = {
        'title': 'Your Pull Request Title',
        'head':  from_branch,
        'base': to_branch,
        'body': 'Description of the pull request',  # PR에 대한 설명
    }

    response = requests.post(
        'https://api.github.com/repos/regulus-foundation/code-mento-test/pulls',
        headers=headers,
        data=json.dumps(data),
    )

    if response.status_code == 201:
        print('Pull request successfully created')
    else:
        print(f'Error: {response.status_code}')
        print(response.text)
    pass
