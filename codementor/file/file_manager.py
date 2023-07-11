import os


def search_files(directory, word):

    found_files = []

    # 사용 예
    directory = './data/project/code-mentor'
    word = 'code-mentor' + ':' + 'comment'
    # found_files = search_files(directory, word)

    if found_files:
        print(f"The word '{word}' was found in the following files:")
        for file in found_files:
            print(file)
    else:
        print(f"The word '{word}' was not found in any files.")

    # 디렉토리의 모든 파일과 하위 디렉토리를 순회합니다.
    for root, dir, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # 각 파일을 열고 지정된 단어를 검색합니다.
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                if word in f.read():
                    found_files.append(file_path)

    return found_files
