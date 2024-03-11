from src.functions import load_data, sorting_executed, sorting_data_time, last_five_actions, masks_the_result, \
    mask_the_result_from
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


def test_masks_the_result():
    """Проверка работоспособности функции для маскировки результата по ключу 'to' """
    data = [
        {'to': 'Счет 96292138399386853355'},
        {'to': 'Maestro 6890749237669619'},
        {'to': 'МИР 2052809263194182'}
    ]
    expected = [
        {'to': 'Счет **3355'},
        {'to': 'Maestro 6890 74** **** 9619'},
        {'to': 'МИР 2052 80** **** 4182'}
    ]
    assert masks_the_result(data) == expected

def test_mask_the_result_from():
    """Проверка работоспособности функции для маскировки результата по ключу 'from' которого
    может и не быть"""
    data = [
        {'id': 1},
        {'id': 2, 'from': 'Счет 96292138399386853355'},
        {'id': 3, 'from': 'Maestro 6890749237669619'},
        {'id': 4, 'from': 'МИР 2052809263194182'}
    ]
    expected = [
        {'id': 1},
        {'id': 2, 'from': 'Счет **3355'},
        {'id': 3, 'from': 'Maestro 6890 74** **** 9619'},
        {'id': 4, 'from': 'МИР 2052 80** **** 4182'}
    ]
    assert mask_the_result_from(data) == expected


