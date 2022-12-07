#!/usr/bin/env python3

from london_co import london_co

def ask():
    input_name = input("Введите имя устройства: ")
    if input_name in london_co.keys():
        print(london_co[input_name])

ask()
