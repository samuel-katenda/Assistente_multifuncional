import os , shutil , platform
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def criar_pasta(nome_pasta):
	"""Está função serve para criar passa"""
	if not nome_pasta or nome_pasta in os.listdir():
		return None
	os.mkdir(nome_pasta)
	return True
	

def criar_pasta_massa(nome_pastas):
		try:
				for pasta in nome_pastas:
					os.makedirs(pasta,exist_ok=True)
		except (PermissionError,OSError):
			pass

def deletar_pasta(pasta_remove=" "):
		try:
			if pasta_remove in os.listdir():
				shutil.rmtree(pasta_remove)
				return True
			return None
		except (NotADirectoryError,PermissionError,OSError):
			return None

def deletar_arquivo(nome_arquivo=" "):
		try:
			if not nome_arquivo in os.listdir():
				return None
			os.remove(nome_arquivo)
			return True
		except IsADirectoryError:
			return None
		
def listar_arquivos():
		if platform.system()=="Linux":
			os.system("ls")
		elif platform.system()=="Windows":
			os.system("dir")
		else:
			return None

def renomear(antigo,novo):
		try:
			os.rename(antigo,novo)
			return True
		except OSError:
			pass
		return None

def pasta_download():
	
	for arquivo in os.listdir("Download"):
		caminho_arquivo=os.path.join("Download", arquivo)
		if arquivo.endswith(".png"):
			criar_pasta("fotos")
			shutil.move(caminho_arquivo, "fotos")
		elif arquivo.endswith(".jpg"):
			shutil.move(caminho_arquivo,"fotos")
		elif arquivo.endswith(".jpeg"):
			shutil.move(caminho_arquivo,"fotos")
		elif arquivo.endswith(".mp4"):
			criar_pasta("Videos")
			shutil.move(caminho_arquivo,"Videos")
		elif arquivo.endswith("mp3"):
			criar_pasta("Musicas")
			shutil.move(caminho_arquivo,"Musicas")
	return None


def inform_arquivo(nome_arquivo):
		if nome_arquivo in os.listdir():
			info=os.stat(nome_arquivo)
			return {
			"arquivo":nome_arquivo,"tamanho(bits)":info.st_size,"acesso":datetime.fromtimestamp(info.st_atime),"modificao":datetime.fromtimestamp(info.st_mtime),"alteracao":datetime.fromtimestamp(info.st_ctime)
			}
		return None
		
		
		
		
