import random


def jogo_da_forca():
    palavras = [
        "python",
        "computador",
        "programacao",
        "internet",
        "algoritmo",
        "terminal"
    ]

    palavra = random.choice(palavras)

    letras_descobertas = ["_" for _ in palavra]
    letras_tentadas = []

    tentativas = 6
    erros_entrada = 0
    limite_erros_entrada = 3

    forca = [
        """
         -----
         |   |
             |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """
    ]


    print("=== JOGO DA FORCA ===")

    while tentativas > 0:

        print(forca[6 - tentativas])
        print("\nPalavra:", " ".join(letras_descobertas))
        print("Letras usadas:", ", ".join(letras_tentadas))
        print("Tentativas restantes:", tentativas)

        letra = input("\nDigite uma letra: ").lower()

        # Verificação de entrada
        if len(letra) != 1 or not letra.isalpha():

            erros_entrada += 1
            print(f"Entrada inválida! ({erros_entrada}/{limite_erros_entrada})")

            if erros_entrada >= limite_erros_entrada:
                tentativas -= 1
                erros_entrada = 0
                print("Muitas entradas inválidas! Perdeste uma tentativa.")

            continue


        if letra in letras_tentadas:
            print("Já tentou essa letra!")
            continue


        letras_tentadas.append(letra)


        if letra in palavra:

            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_descobertas[i] = letra

            print("Boa! A letra existe.")

        else:
            tentativas -= 1
            print("Errado!")


        if "_" not in letras_descobertas:
            print("\nParabéns! Descobriste a palavra:", palavra)
            return


    print(forca[6])
    print("\nPerdeste! A palavra era:", palavra)



