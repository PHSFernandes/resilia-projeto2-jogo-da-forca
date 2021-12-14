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


def preencher_lista_jogadores(quantidade):
    lista_jogadores = []
    for n in range(quantidade):
        nome = input(f"Escolha o nome do jogador {n + 1}: ").title()
        while nome == "" or nome.isspace():
            nome = input(f"Preencha o nome do jogador {n + 1}: ").title()
        else:
            lista_jogadores.append(Jogador(nome))

    return lista_jogadores


def jogador_acertou(jogador_atual):
    jogador_atual.substituir_adivinhacao_por_letra()
    jogador_atual.acertos = len(jogador_atual.palavra) - jogador_atual.adivinhacao.count("_")


def jogador_venceu(jogador_atual):
    screen_clear()
    jogador_atual.template()
    print(f"{jogador_atual.nome} venceu o jogo, parabéns!")
    time.sleep(1)


def jogador_errou(jogador_atual):
    jogador_atual.vidas -= 1
    screen_clear()
    jogador_atual.template()
    print("Você errou")
    time.sleep(1)


def verificar_chute_valido(jogador_atual):
    if len(jogador_atual.chute) > 1 or jogador_atual.chute.isalpha() is False:
        print("Escolha APENAS uma letra!")

    elif jogador_atual.chute.upper() in jogador_atual.letras_erradas or jogador_atual.chute in jogador_atual.adivinhacao:
        print("Você já escolheu esta letra. Tente outra.")

    time.sleep(1)


def jogador_sem_vida(jogador_atual, perdedores):
    print(f"{jogador_atual.nome} está fora do jogo. A palavra era {jogador_atual.palavra.upper()}")
    perdedores.append(jogador_atual)
    time.sleep(2)
