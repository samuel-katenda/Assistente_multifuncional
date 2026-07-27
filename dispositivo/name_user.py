import json

# a função arquivo() abri um ficheiro json onde tem o nome do usuario
def arquivo():
	try:
		with open("usuario.json", "r", encoding="utf-8")as arquivo:
			infor=json.load(arquivo)
			return infor
	except json.decoder.JSONDecodeError:
		pass
	except FileNotFoundError:
		pass
	return None

# a função registar() serve para colocar o nome do usuario em um arquivo json caso o nome ainda não foi guardado
def registar(nome):
	with open("usuario.json","w", encoding="utf-8") as user:
		json.dump(nome,user, indent=4,ensure_ascii=False)
	
	
