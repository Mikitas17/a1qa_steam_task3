import os

download_dir = "D:\\downloads"


def is_file_downloaded(file):
    for _, _, file_list in os.walk(download_dir):
        if file in file_list:
            return True
    return False
