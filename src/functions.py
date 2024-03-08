import json
import pprint
from config import ROOT_DIR
import os
import datetime
pp = pprint.PrettyPrinter(indent=7)

operation_path = os.path.join(ROOT_DIR, "src", 'operations.json')

def load_data(operation_path):
    """функция распаковки файла json"""
    with open(operation_path, 'r') as file:
        file = json.loads(file.read())
    return file

#pp.pprint(load_data(operation_path))



def sorting_executed(file):
    """сортировка выполненных операций"""
    new_list = []
    for element in file:
        if element and element["state"] == "EXECUTED":
            new_list.append(element)
    return new_list

new_list = sorting_executed(load_data(operation_path))
#pp.pprint(sorting_executed(load_data(operation_path)))

def sorting_data_time(new_list):
    """Функция сортирует по дате и выводит дату в формате ДД.ММ.ГГГГ"""
    new_list.sort(key=lambda x: x.get("date"), reverse=True)
    for element in new_list:
        element["date"] = datetime.datetime.strptime(element["date"], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    return new_list


#pp.pprint(sorting_data_time(new_list))

