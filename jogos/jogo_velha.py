import random

def jogo_da_velha():
    tabuleiro = [" " for _ in range(9)]

    def mostrar_tabuleiro():
        print()
        print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
        print("--+---+--")
        print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
        print("--+---+--")
        print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")
        print()

    def verificar_vitoria(jogador):
        vitorias = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
            [0, 4, 8], [2, 4, 6]              # diagonais
        ]

        for combinacao in vitorias:
            if (tabuleiro[combinacao[0]] == jogador and
                tabuleiro[combinacao[1]] == jogador and
                tabuleiro[combinacao[2]] == jogador):
                return True

        return False

    def jogada_jogador():
        while True:
            posicao = int(input("Escolha uma posição (1-9): ")) - 1

            if 0 <= posicao <= 8 and tabuleiro[posicao] == " ":
                tabuleiro[posicao] = "X"
                break
            else:
                print("Posição inválida!")

    def jogada_computador():
        livres = []

        for i in range(9):
            if tabuleiro[i] == " ":
                livres.append(i)

        escolha = random.choice(livres)
        tabuleiro[escolha] = "O"

    def empate():
        return " " not in tabuleiro

    while True:
        mostrar_tabuleiro()

        jogada_jogador()

        if verificar_vitoria("X"):
            mostrar_tabuleiro()
            print("Vitória do jogador!")
            break

        if empate():
            mostrar_tabuleiro()
            print("Empate!")
            break

        jogada_computador()

        if verificar_vitoria("O"):
            mostrar_tabuleiro()
            print("Vitória do computador!")
            break

        if empate():
            mostrar_tabuleiro()
            print("Empate!")
            break