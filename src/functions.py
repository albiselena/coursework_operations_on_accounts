import json
import pprint
from config import ROOT_DIR
import os
import datetime
pp = pprint.PrettyPrinter(indent=4)

operation_path = os.path.join(ROOT_DIR, "src", 'operations.json')

def load_data(operation_path):
    """функция распаковки файла json"""
    with open(operation_path, 'r') as file:
        file = json.loads(file.read())
    return file

#pp.pprint(load_data(operation_path))



def sorting_executed(file):
    """сортировка выполненных операций"""
    validated = []
    for element in file:
        if element and element["state"] == "EXECUTED":
            validated.append(element)
    return validated

validated = sorting_executed(load_data(operation_path))
#pp.pprint(sorting_executed(load_data(operation_path)))

def sorting_data_time(validated):
    """Функция сортирует по дате и выводит дату в формате ДД.ММ.ГГГГ"""
    validated.sort(key=lambda x: x.get("date"), reverse=True)
    for element in validated:
        element["date"] = datetime.datetime.strptime(element["date"], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    return validated

#print(sorting_data_time(new_list))
#pp.pprint(sorting_data_time(validated))
def last_five_actions(validated):
    """Функция возвращает последние 5 операций и их описание"""
    return validated[:5]

pp.pprint(last_five_actions(sorting_data_time(validated)))


