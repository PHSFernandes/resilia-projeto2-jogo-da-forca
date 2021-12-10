import time
from jogadores import Jogador
from funcoes import screen_clear

quantidade_jogadores = input("Quantos jogadores irão participar (2 a 4)? ")

while quantidade_jogadores.isdigit() is False or int(quantidade_jogadores) > 4 or int(quantidade_jogadores) < 2:
    screen_clear()
    quantidade_jogadores = input("Selecione um valor válido (2 a 4): ")

lista_jogadores = []
for n in range(int(quantidade_jogadores)):
    nome = input(f"Escolha o nome do jogador {n + 1}: ").title()
    while nome == "" or nome.isspace():
        nome = input(f"Preencha o nome do jogador {n + 1}: ").title()
    else:
        lista_jogadores.append(Jogador(nome))

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
                        jogador.substituir_adivinhacao_por_letra()
                        jogador.acertos = len(jogador.palavra) - jogador.adivinhacao.count("_")
                        if jogador.checar_se_vencedor():
                            screen_clear()
                            jogador.template()
                            print(f"{jogador.nome} venceu o jogo, parabéns!")
                            time.sleep(1)
                            continua = False
                            break
                        else:
                            continue
                    else:
                        jogador.vidas -= 1
                        screen_clear()
                        jogador.template()
                        print("Você errou")
                        time.sleep(1)
                else:
                    if len(jogador.chute) > 1 or jogador.chute.isalpha() is False:
                        print("Escolha APENAS uma letra!")
                        time.sleep(1)
                        continue
                    elif jogador.chute.upper() in jogador.letras_erradas or jogador.chute in jogador.adivinhacao:
                        print("Você já escolheu esta letra. Tente outra.")
                        time.sleep(1)
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
