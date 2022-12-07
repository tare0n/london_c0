#!/usr/bin/env python3

from london_co import london_co

def ask():
    input_name = input("Введите имя устройства: ")
    if input_name in london_co.keys():
        input_param = input(f"Введите имя параметра: {[key for key in london_co[input_name].keys()]} ")
        if input_param in london_co[input_name].keys():
            print(london_co[input_name][input_param])
        else:
            print("Такого параметра нет")

ask()
