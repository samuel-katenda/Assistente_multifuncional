import json

# Estas funções acedem às chaves (tokens) armazenadas em ficheiros JSON.
# Depois de definires o caminho para os ficheiros JSON, basta chamares
# estas funções na tua API para obteres os respetivos tokens.		

def chave_clima():
	with open("nome_do_caminho_do_api_key_json","r") as arquivo:
		return json.load(arquivo)
		
def chave_ia():
	with open("nome_do_caminho_do_api_key_json","r",encoding="utf-8") as arquivo:
		return json.load(arquivo)

def chave_cambio():
	with open("nome_do_caminho_do_api_key_json","r") as arquivo:
		return json.load(arquivo)
		
	
