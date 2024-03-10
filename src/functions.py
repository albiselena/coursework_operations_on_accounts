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


#pp.pprint(sorting_data_time(validated))
def last_five_actions(validated):
    """Функция возвращает последние 5 операций и их описание"""
    return validated[:30]

ss =  last_five_actions(sorting_data_time(validated))
#pp.pprint(ss)

def masks_the_result(ss):
    """Функция маскирует результат"""
    for index in ss:
        if 'Счет' in index["to"] :
            index["to"] = index["to"][:5] + "**" + index["to"][-4:]
        else:
            index["to"] = index["to"][0:-12] + " " + index["to"][-13:-11] + "**" + " " + "****" + " " + index["to"][-5:-1]
    return ss
#Visa Platinum 7000 79** **** 6361

nn = masks_the_result(ss)
#pp.pprint(nn)

def formatted_information(nn):
    """Функция вывода информации в читаемом виде"""
    for index in nn:
        if index.get('from') is not None:
            print(f"{index['date']} {index['description']}\n"
                  f"{index.get('from')} -> {index['to']}\n"
                  f"{index['operationAmount']['amount']} {index['operationAmount']['currency']['name']}\n")
        if index.get('from') is None:
            print(f"{index['date']} {index['description']}\n"
                  f"{index['to']}\n"
                  f"{index['operationAmount']['amount']} {index['operationAmount']['currency']['name']}\n")

formatted_information(nn)




