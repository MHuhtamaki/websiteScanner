import os


def create_directory(directory_name):

    if not os.path.exists(directory_name):
        os.makedirs(directory_name)


def write_file(path, data):
    with open(path, 'a+') as file:
        file.write(data)
