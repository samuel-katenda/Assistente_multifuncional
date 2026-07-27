import random

def batalha_naval():
    tamanho = 5

    # Criar tabuleiro
    tabuleiro = [["~" for _ in range(tamanho)] for _ in range(tamanho)]

    # Colocar navio do computador
    navio_linha = random.randint(0, tamanho - 1)
    navio_coluna = random.randint(0, tamanho - 1)

    tentativas = 10

    print("=== BATALHA NAVAL ===")
    print("Encontre o navio inimigo!")
    print("O tabuleiro tem tamanho 5x5")

    while tentativas > 0:
        print()

        # Mostrar tabuleiro
        for linha in tabuleiro:
            print(" ".join(linha))

        print(f"\nTentativas restantes: {tentativas}")

        try:
            linha = int(input("Escolha a linha (0-4): "))
            coluna = int(input("Escolha a coluna (0-4): "))

            if linha < 0 or linha >= tamanho or coluna < 0 or coluna >= tamanho:
                print("Posição inválida!")
                continue

            if tabuleiro[linha][coluna] != "~":
                print("Já tentaste essa posição!")
                continue

            if linha == navio_linha and coluna == navio_coluna:
                tabuleiro[linha][coluna] = "X"
                print("\n🚢 Acertaste no navio! Vitória!")
                return

            else:
                tabuleiro[linha][coluna] = "O"
                print("Água! Não acertaste.")

            tentativas -= 1

        except ValueError:
            print("Digite apenas números!")

    print("\nFim do jogo!")
    print(f"O navio estava em: linha {navio_linha}, coluna {navio_coluna}")
