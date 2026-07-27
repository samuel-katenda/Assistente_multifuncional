def jogo_2048():
    import random
    import os

    tamanho = 4

    def limpar():
        os.system("cls" if os.name == "nt" else "clear")

    def mostrar(tab):
        limpar()
        print("=== 2048 ===\n")

        for linha in tab:
            print("+----" * tamanho + "+")
            for n in linha:
                print(f"|{n:^4}" if n else "|    ", end="")
            print("|")

        print("+----" * tamanho + "+")
        print("\nW cima | S baixo | A esquerda | D direita | Q sair")


    def adicionar(tab):
        vazios = []

        for i in range(tamanho):
            for j in range(tamanho):
                if tab[i][j] == 0:
                    vazios.append((i, j))

        if vazios:
            i, j = random.choice(vazios)
            tab[i][j] = 2


    def mover(linha):
        linha = [x for x in linha if x != 0]

        resultado = []
        i = 0

        while i < len(linha):
            if i + 1 < len(linha) and linha[i] == linha[i+1]:
                resultado.append(linha[i] * 2)
                i += 2
            else:
                resultado.append(linha[i])
                i += 1

        while len(resultado) < tamanho:
            resultado.append(0)

        return resultado


    tabuleiro = [[0]*tamanho for _ in range(tamanho)]

    adicionar(tabuleiro)
    adicionar(tabuleiro)

    while True:
        mostrar(tabuleiro)

        comando = input("> ").lower()

        if comando == "q":
            break

        if comando == "a":
            for i in range(tamanho):
                tabuleiro[i] = mover(tabuleiro[i])

        elif comando == "d":
            for i in range(tamanho):
                tabuleiro[i] = mover(tabuleiro[i][::-1])[::-1]

        elif comando == "w":
            colunas = list(zip(*tabuleiro))

            novas = []
            for c in colunas:
                novas.append(mover(list(c)))

            tabuleiro = [list(x) for x in zip(*novas)]

        elif comando == "s":
            colunas = list(zip(*tabuleiro))

            novas = []
            for c in colunas:
                novas.append(mover(list(c)[::-1])[::-1])

            tabuleiro = [list(x) for x in zip(*novas)]

        adicionar(tabuleiro)


