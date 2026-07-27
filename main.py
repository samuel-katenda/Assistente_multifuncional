from dispositivo import name_user
import menu_sistema as menu
import controle
import os

nome_usuario=name_user.arquivo()
def linha():
	print("=-=-=-=-=-=-=-=-=-=-=-=-=")	
	
if not nome_usuario:
	nome=input("Digite o teu nome:")
	name_user.registar(nome)
	print("carregando na proxima execução...")
else:
	print(f"Olá {nome_usuario} o que vamos fazer !")
linha()
print("0-Limpar a tela")
print("1-Manipular ficheiros")
print("2-Serviços da internet")
print("3-Manipular sistema")
print("4-Jogar jogos de terminal.")
codigo_opcao=("1","2","3","4","5","6","7","8","9")
while True:
	opcao=input(f"Digite a tua opção {nome_usuario}:")
	match opcao:
			case "1":
				linha()
				menu.ficheiros_menu()
				opcao=input(f"Digite a tua opção:")
				if opcao in codigo_opcao[0:8]:
					controle.opcao_ficheiros(opcao)
				else:
					print("Não tenho essa funcionalidade em ficheiros.")

			case "2":
				linha()
				menu.internet_menu()
				opcao=input("Digite a tua opção:")
				if opcao in codigo_opcao[0:6]:
					controle.opcao_internet(opcao)
				else:
					print("Não tenho essa funcionalidade na internet.")
			case "3":
				linha()
				menu.sistema_menu()
				opcao=input("Digite a tua opção:")
				if opcao in codigo_opcao[0:6]:
					controle.opcao_sistema(opcao)
				else:
					print("Não tenho essa funcionalidade no sistema.")
					
			case "4":
			 	linha()
			 	menu.jogos_menu()
			 	opcao=input("Digite a tua opção:")
			 	if opcao in codigo_opcao[0:7]:
			 		controle.opcao_jogos(opcao)
			 	else:
			 		print("Não tenho essa funcionalidade nos jogos.")
			
			case "0":
				os.system("clear")
			case _:
				print("Não tenho essa opção.")
