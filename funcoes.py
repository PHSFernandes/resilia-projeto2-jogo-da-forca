import sys
import time
import elementos
import random
from os import system, name


def screen_clear():
    """Esta função limpa o terminal"""
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def sorteio_palavra():
    sorteio = random.choice(elementos.lista_palavras).lower()
    return sorteio


def seleciona_quantidades_de_jogadores():
    quantidade_jogadores = input("Quantos jogadores irão participar (2 a 4)? ")

    while quantidade_jogadores.isdigit() is False or int(quantidade_jogadores) > 4 or int(quantidade_jogadores) < 2:
        screen_clear()
        quantidade_jogadores = input("Selecione um valor válido (2 a 4): ")

    return int(quantidade_jogadores)
