import time
from jogadores import Jogador
from funcoes import print_slow, screen_clear, seleciona_quantidades_de_jogadores
from elementos import logo

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

print_slow(logo)

quantidade_jogadores = seleciona_quantidades_de_jogadores()

lista_jogadores = preencher_lista_jogadores(quantidade_jogadores)

print(lista_jogadores)
time.sleep(1)

continua = True
lista_perdedores = []


for n in range(6):
    for jogador in lista_jogadores:
        if jogador not in lista_perdedores:
            while continua:
                jogador.responder()
                if jogador.checar_se_chute_valido():
                    if jogador.checar_se_acertou():
                        jogador_acertou(jogador)
                        if jogador.checar_se_vencedor():
                            jogador_venceu(jogador)
                            continua = False
                            break
                        else:
                            continue
                    else:
                        jogador_errou(jogador)
                else:
                    verificar_chute_valido(jogador)
                    continue

                # Se o jogador perder todas as vidas, é removido do jogo
                if jogador.vidas == 0:
                    print(f"{jogador.nome} está fora do jogo. A palavra era {jogador.palavra.upper()}")
                    lista_perdedores.append(jogador)
                    time.sleep(2)

                # Se não houver mais jogadores na partida, o jogo é automaticamente finalizado
                if len(lista_jogadores) == len(lista_perdedores):
                    print("Nenhum jogador venceu")
                    continua = False
                    time.sleep(1)
                break
