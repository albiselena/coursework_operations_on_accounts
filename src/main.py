from functions import *


def main():
    for index in ready_dictionary:
        if index.get('from') is not None:
            print(f"{index['date']} {index['description']}\n"
                  f"{index.get('from')} -> {index['to']}\n"
                  f"{index['operationAmount']['amount']} {index['operationAmount']['currency']['name']}\n")
        if index.get('from') is None:
            print(f"{index['date']} {index['description']}\n"
                  f"{index['to']}\n"
                  f"{index['operationAmount']['amount']} {index['operationAmount']['currency']['name']}\n")


if __name__ == "__main__":
    main()
