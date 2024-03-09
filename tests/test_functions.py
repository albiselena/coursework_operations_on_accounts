from src.functions import load_data, sorting_executed, sorting_data_time, last_five_actions
from config import ROOT_DIR
import os


def test_load_data():
    """Проверка работоспособности распаковки файла json"""
    operation_path = os.path.join(ROOT_DIR, "src", 'operations.json')
    assert type(load_data(operation_path) == list and len(load_data(operation_path)) > 0)
    assert type(load_data(operation_path)[0]) == dict
    assert type(load_data(operation_path)[0]['state']) == str
    assert type(load_data(operation_path)[34]['id']) == int


def test_sorting_executed():
    """Проверка работоспособности сортировки по ключы state выполенной операций"""
    data = [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELED"}, {"id": 3, "state": "EXECUTED"}]
    expected = [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}]
    assert sorting_executed(data) == expected


def test_sorting_data_time():
    """Проверка сортировки по дате"""
    data = [
        {"id": 1, 'date': '2022-01-13T13:00:58.458625'},
        {"id": 2, 'date': '2024-01-23T01:48:30.477053'},
        {"id": 3, 'date': '2023-01-21T01:10:28.317704'}
    ]
    expected = [
        {"id": 2, 'date': '23.01.2024'},
        {"id": 3, 'date': '21.01.2023'},
        {"id": 1, 'date': '13.01.2022'}
    ]
    assert sorting_data_time(data) == expected


def test_last_five_actions():
    """Проверка работоспособности функции для вывода последних 5 операций"""
    data = [
        {"id": 1, 'state': 'EXECUTED'},
        {"id": 2, 'state': 'CANCELED'},
        {"id": 3, 'state': 'EXECUTED'},
        {"id": 4, 'state': 'EXECUTED'},
        {"id": 5, 'state': 'EXECUTED'},
        {"id": 6, 'state': 'EXECUTED'},
        {"id": 7, 'state': 'EXECUTED'}
    ]
    expected = [
        {"id": 1, 'state': 'EXECUTED'},
        {"id": 2, 'state': 'CANCELED'},
        {"id": 3, 'state': 'EXECUTED'},
        {"id": 4, 'state': 'EXECUTED'},
        {"id": 5, 'state': 'EXECUTED'}
    ]
    assert last_five_actions(data) == expected

