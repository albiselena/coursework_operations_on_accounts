import json
from config import ROOT_DIR
import os
import datetime

# путь к файлу с операциями и файлу с данными о клиентах и т.д.
operation_path = os.path.join(ROOT_DIR, "src", 'operations.json')


def load_data(operation_path):
    """Функция распаковки файла json"""
    with open(operation_path, 'r') as file:
        file = json.loads(file.read())
    return file


def sorting_executed(file):
    """Сортировка выполненных операций по ключу state, если операция выполнена EXECUTED
    перекладываю в другой словарь"""
    validated = []
    for element in file:
        if element and element["state"] == "EXECUTED":
            validated.append(element)
    return validated


# переменная validated с отсортированным словарём с выполненными операциями
validated = sorting_executed(load_data(operation_path))


def sorting_data_time(validated):
    """Функция сортирует по дате(от последних операций к более старым)
    и переводит дату в формат ДД.ММ.ГГГГ"""
    validated.sort(key=lambda x: x.get("date"), reverse=True)
    for element in validated:
        element["date"] = datetime.datetime.strptime(element["date"], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    return validated


def last_five_actions(validated):
    """Функция возвращает последние 5 операций и их описание
    по срезу, который в случае необходимости достаточно поменять"""
    return validated[:5]


# переменная с датой в нужном формате
validated_dated = last_five_actions(sorting_data_time(validated))


def masks_the_result(validated_dated):
    """Функция маскирует результат по ключу 'to'. Если в значении есть слово 'Счет' маскирует:
    **XXXX, если же карты тогда: XXXX XX** **** XXXX"""
    for index in validated_dated:
        if 'Счет' in index["to"]:
            index["to"] = index["to"][:5] + "**" + index["to"][-4:]
        else:
            index["to"] = (index["to"][0:-12] + " " + index["to"][-12:-10] + "**" + " "
                           + "****" + " " + index["to"][-4:])
    return validated_dated


def mask_the_result_from(masks_the_result):
    """Функция маскирует результат по ключу 'from'. Если ключ 'from' существует в словаре и
    если в значении есть слово 'Счет' маскирует: **XXXX, если же любые карты тогда: XXXX XX** **** XXXX"""
    for index in masks_the_result:
        if index.get('from') is not None:
            if 'Счет' in index["from"]:
                index["from"] = index["from"][:5] + "**" + index["from"][-4:]
            else:
                index["from"] = (index["from"][0:-12] + " " + index["from"][-12:-10] + "**" + " "
                                 + "****" + " " + index["from"][-4:])
    return masks_the_result


# переменная со словарём уже замаскированных данных карт и счетов
ready_dictionary = mask_the_result_from(masks_the_result(validated_dated))
