import os


def search_files(directory):

    found_files = []
    word = 'code-mentor' + ':' + 'docs'
    # found_files = search_files(directory, word)

    # 디렉 토리의 모든 파일과 하위 디렉 토리를 순회 합니다.
    for root, dir, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # 각 파일을 열고 지정된 단어를 검색합니다.
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                if word in f.read():
                    found_files.append(file_path)

    return found_files
