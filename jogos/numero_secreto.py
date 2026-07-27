from random import randint


def play_secreto():
	print("GEREI UM NÚMERO ENTRE 1 à 15 QUAL É ?")
	secreto_numero=randint(1,15)
	tentativa=5
	while tentativa>0:
			try:
				digite_palpite=int(input("Digite o teu palpite:"))
				if digite_palpite>secreto_numero:
					print("Muito alto")
					tentativa-=1
					print(f"Restam {tentativa} tentativas")
				elif digite_palpite<secreto_numero:
					print("Muito baixo")
					tentativa-=1
					print(f"Restam {tentativa} tentativas")
				else:
					print(f"Acertaste o número era {secreto_numero}")
					break
				if tentativa==0:
					print("JOGO TERMINADO")
					break
			except ValueError:
				print("Por favor digite um número")
				