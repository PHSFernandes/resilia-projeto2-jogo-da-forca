import time
import unidecode
from funcoes import screen_clear, sorteio_palavra


class Jogador:
    def __init__(self, nome): 
        self.nome = nome
        self.vidas = 6
        self.acertos = 0
        self.palavra = sorteio_palavra()
        self.adivinhacao = ["_" for _ in self.palavra]
        self.letras_erradas = []
        self.chute = ""

    def __repr__(self):
        return f"Jogador {self.nome}"

    def responder(self):
        """A rotina básica de adivinhação"""
        screen_clear()
        self.template()
        self.chute = unidecode.unidecode(input("Escolha uma letra: ")).lower()

    def checar_se_acertou(self):
        """Verifica se o jogador acertou o chute"""
        if self.chute in unidecode.unidecode(self.palavra) and self.chute not in self.adivinhacao:
            return True
        else:
            self.letras_erradas.append(self.chute.upper())
            return False

    def substituir_adivinhacao_por_letra(self):
        """Troca os underlines pela letra adivinhada"""
        for n in range(len(self.palavra)):
            if self.chute == unidecode.unidecode(self.palavra[n]):
                self.adivinhacao[n] = self.palavra[n]

    def checar_se_vencedor(self):
        """Esta função checa se o jogador venceu o jogo e retorna True caso verdadeiro"""
        if self.acertos == len(self.palavra):
            return True

    def mostrar_adivinhacoes(self):
        """Mostra os underlines de letras a serem adivinhadas"""
        for _ in self.adivinhacao:
            print(_.upper(), end=" ")
        print()
        print("Letras erradas:")
        for _ in self.letras_erradas:
            print(_.upper(), end=" ")

    def checar_se_chute_valido(self):
        """Verifica se a letra chutada é valida (se não é número ou se é mais de uma letra)."""
        if (len(self.chute) > 1 or self.chute.isalpha() == False) or \
                (self.chute.upper() in self.letras_erradas or self.chute in self.adivinhacao):
            return False
        else:
            return True

    def template(self):
        # print(f"{self.nome}: {self.palavra}\n")
        print(f"Vez de {self.nome}:")
        self.desenha_forca()
        self.mostrar_adivinhacoes()
        print()

    def desenha_forca(self):
        """Desenho da forca correspondente a cada vida"""
        if self.vidas == 6:
            print("  _______     ")
            print(" |/      |    ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        elif self.vidas == 5:
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        elif self.vidas == 4:
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |       |    ")
            print(" |       |    ")
            print(" |            ")

        elif self.vidas == 3:
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      \|   ")
            print(" |       |    ")
            print(" |            ")

        elif self.vidas == 2:
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        elif self.vidas == 1:
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        elif self.vidas == 0:
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")
