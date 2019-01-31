import random

tabuleiro = ['''

>>>>>>>>>>Forca<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


class Forca:

    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_acertadas = []

    def advinhar_letra(self, letra):
        if letra in self.palavra and letra not in self.letras_acertadas:
            self.letras_acertadas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        elif letra in self.letras_acertadas or letra in self.letras_erradas:
            print("Você já informou esta letra anteriormente. Por favor informar uma letra diferente!")
        else:
            return False
        return True

    def jogo_acabou(self):
        return self.ganhou() or (len(self.letras_erradas) == 6)

    def ganhou(self):
        if '_' not in self.palavra_secreta():
            return True
        return False

    def palavra_secreta(self):
        composicao = ' '
        for letra in self.palavra:
            if letra not in self.letras_acertadas:
                composicao += '_ '
            else:
                composicao += letra
        return composicao

    def status_jogo(self):
        print(tabuleiro[len(self.letras_erradas)])
        print("\nPalavra: " + self.palavra_secreta())
        print("\nLetras erradas: ",)
        for letra in self.letras_erradas:
            print(letra,)
        print()
        print("\nLetras corretas: ",)
        for letra in self.letras_acertadas:
            print(letra,)
        print()


def mensagem_abertura():
        print("Bem vindo ao jogo da Forca!")


def palavra_aleatoria():
    with open("palavras.txt", "r") as a:
        arquivo = a.readlines()
    return arquivo[random.randint(0, len(arquivo))].strip()


def execucao_programa():
    mensagem = Forca(mensagem_abertura())
    print(mensagem)

    game = Forca(palavra_aleatoria())

    while not game.jogo_acabou():
        game.status_jogo()
        inserir_letra = input("\nDigite uma letra: ").lower()
        game.advinhar_letra(inserir_letra)

    game.status_jogo()

    if game.ganhou():
        print("\nParabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("\nPuxa, você foi enforcado!")
        print("A palavra era: " + game.palavra)
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

    print('\nObrigada por jogar conosco!\n')


if __name__ == "__main__":
    execucao_programa()

