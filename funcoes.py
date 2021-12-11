from os import system, name
from time import sleep


def screen_clear():
    """Esta função limpa o terminal"""
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


