import json


def read_file(file_name):
    with open(file_name, 'r') as file:
        d = json.load(file)
    return d

