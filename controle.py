import dispositivo.ficheiros as file
import os
from  internet.clima import estado_tempo
from internet.bitcoin import monitorar_bitcoin
from internet.conversor_moedas import cambio
from internet.ia import sistema_ia
from internet.navegador import abrir_site
from jogos.batalhanaval import batalha_naval
from jogos.numero_secreto import play_secreto
from jogos.jogo_2048 import jogo_2048
from jogos.forca import jogo_da_forca
from jogos.jogo_velha import jogo_da_velha
from jogos.calculadora_basico import calculadora
from menu_sistema import alguns_prog
import dispositivo.sistema as system
from dispositivo.informacoes import infor_sistema

def opcao_ficheiros(pedido):
    match pedido:

        case "1":
            nome_pasta = input("Digite o nome da pasta a ser criada: ")
            criar = file.criar_pasta(nome_pasta)

            if not criar:
                print("Não foi possível criar a pasta.")
            else:
                print(f"Pasta {nome_pasta} criada com sucesso.")

        case "2":
            try:
                pastas = []
                quant = int(input("Quantas pastas queres criar: "))

                for pasta in range(1, quant + 1):
                    nome = input(f"Nome da {pasta}ª pasta: ")
                    pastas.append(nome)

                file.criar_pasta_massa(pastas)
                print("Pastas criadas com sucesso.")

            except ValueError:
                print("Quantidade de pastas inválida.")

        case "3":
            deletar = input("Digite o nome da pasta a deletar: ")

            if not file.deletar_pasta(deletar):
                print(f"Não foi possível deletar a pasta {deletar}.")
            else:
                print(f"Pasta {deletar} deletada com sucesso.")

        case "4":
            arquivo = input("Digite o nome do arquivo a deletar: ")
            deletar = file.deletar_arquivo(arquivo)

            if not deletar:
                print("Não foi possível deletar o arquivo.")
            else:
                print(f"Arquivo {arquivo} deletado com sucesso.")

        case "5":
            listar = file.listar_arquivos()
            if not listar:
            	print("Não foi possivel listar os arquivos !")
            else:
            	file.listar_arquivos()

        case "6":
            antigo = input("Digite o nome do arquivo a renomear: ")

            if antigo in os.listdir():
                novo = input("Digite o novo nome: ")

                if not novo in os.listdir():
                    reno = file.renomear(antigo, novo)

                    if not reno:
                        print(f"Não foi possível renomear o ficheiro {antigo}.")
                    else:
                        print(f"Ficheiro {antigo} renomeado para {novo} com sucesso.")
                else:
                    print(f"Já existe um arquivo com o nome {novo}.")
            else:
                print(f"O arquivo {antigo} não existe.")

        case "7":
            if not file.pasta_download():
                print("Pasta Download organizada com sucesso.")

        case "8":
            nome_arquivo = input("Digite o nome do arquivo: ")
            infor = file.inform_arquivo(nome_arquivo)

            if not infor:
                print("Não foi possível obter as informações.")
            else:
                print("=-=-=-=-=-=-=-=-=-=-=-=")
                for chave, dados in infor.items():
                	print(f"{chave}: {dados}")


def opcao_internet(pedido):

    match pedido:
        case "1":
            cidade = input("Digite o nome da cidade: ")
            print("=-=-=-=-=-=-=-=-=-=-=-=")
            estado_tempo(cidade)

        case "2":
            monitorar_bitcoin()

        case "3":
            moeda = input("Digite o código da moeda: ")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=")
            cambio(moeda)

        case "4":
            while True:
                pergunta = input("Faça a tua pergunta à IA: ")
                print("-=-=-=-=-=-=-=-=-=-=-=-=")
                resposta = sistema_ia(pergunta)
                print(resposta)

                sair = input("Queres sair (sim/não): ")
                if sair == "sim":
                    break

        case "5":
            print("""
Escolha o teu site para navegar:
    1 - Google
    2 - Gemini
    3 - ChatGPT
    4 - GitHub
    5 - YouTube
    6 - SnapSave
    7 - Facebook
    8 - Claude
    9 - Canva
    10 - Drive
""")

            digite = input("Digite a tua opção: ")
            abrindo = abrir_site(digite)
            if not abrindo:
            	print("Não foi possivel abrir o site !")
 


def opcao_jogos(pedido):
            match pedido:
            	case "1":
            		batalha_naval()
            	case "2":
            		play_secreto()
            	case "3":
            		jogo_2048()
            	case "4":
            		jogo_da_forca()
            	case "5":
            		jogo_da_velha()
            		
            	case "6":
            		try:
            			while True:
            				valor1=int(input("Digite o primeiro valor:"))
            				valor2=int(input("Digite o segundo valor:"))
            				opcao=input("Digite a operação:")
            				resposta = calculadora(opcao,valor1,valor2)
            				if not resposta:
            					print("Não foi possivel fazer a operação")
            				else:
            					print(f"{valor1} {opcao} {valor2} = {resposta}")
            				sair=input("Queres sair (sim/não):").lower()
            				if sair == "sim":
            					break
            		except ValueError:
            			print("valor inválido para o cálculo")
            		

def opcao_sistema(pedido):
            				  match pedido:
            				  	case "1":
            				  		print("=-=-=-=-=-=-=-=-=-=-=")
            				  		alguns_prog()
            				  		opcao=input("Digite a tua opção:")
            				  		if opcao=="15":
            				  			app=input("Digite o programa a ser aberto:")
            				  			prog=system.abrir_programa(app)
            				  			if not prog:
            				  				print("Não foi possivel abrir o programa !")
            				  		else:
            				  			prog=system.abrir_programa(opcao)
            				  			
            				  			if not prog:
            				  				print("Não foi possivel abrir o programa !")
            				  	
            				  	case "2":
            				  			print("=-=-=-=-=-=-=-=-=")
            				  			system.listar_processos()
            				  	
            				  	case "3":
            				  			nome_programa=input("Digite o nome do programa:")
            				  			fechar=system.fechar_programa(nome_programa)
            				  			if not fechar:
            				  				print(f"Não foi possivel fechar o programa {nome_programa}.")
            				  			else:
            				  				print("Fechado com sucesso o programa {nome_programa}.")
            				  	case "4":
            				  			desligar=system.desligar_sistema()
            				  			if not desligar:
            				  				print("Não foi possivel desligar o dispositivo.")
            				  				
            				  	case "5":
            				  			reiniciar=system.reiniciar_sistema()
            				  			if not reiniciar:
            				  				print("Não foi possivel reiniciar o dispositivo")
            				  	case "6":
            				  			print("=-=-=-=-=-=-=-=-=-=")
            				  			infor_sistema()	
            				  			
            				  			
            				  
            				     		
            		
            		
            		
            		
            		
            
            	
	