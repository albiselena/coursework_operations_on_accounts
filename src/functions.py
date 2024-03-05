import json


def load_data():
    """распаковка файла json"""
    with open('operations.json', 'r') as file:
        file = json.loads(file.read())
    return file



