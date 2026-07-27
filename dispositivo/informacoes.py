import os , shutil, psutil,subprocess, socket, platform

def armazenamento():
	armazenar=shutil.disk_usage(os.getcwd())
	return {"armazenamento total": armazenar.total,"usado":armazenar.used,"restante":armazenar.free
	}
	
def memoria():
	memory=psutil.virtual_memory ()
	return {
	"memoria total":memory.total,"usado":memory.used,
	"restante":memory.available
	}

def cpu():
	arquitetura=subprocess.check_output(["getprop", "ro.product.cpu.abi"],text=True).strip()
	logico=psutil.cpu_count(logical=True)
	fisico=psutil.cpu_count(logical=False)
	return {
	"total de nucleos fisicos":fisico,"total de nucleos logicos":logico,"arquitetura do processador":arquitetura
	}

def dispositivo():
    try:
        modelo = subprocess.check_output(
            ["getprop", "ro.product.model"],
            text=True
        ).strip()

        marca = subprocess.check_output(
            ["getprop", "ro.product.brand"],
            text=True
        ).strip()
        versao=subprocess.check_output(["getprop","ro.build.version.release"],text=True).strip()
        
        return {
        "modelo":modelo,"marca":marca,"versao_sistema":versao
        }

    except Exception:
        return None
    
def bateria():
	try:
		battery=psutil.sensors_battery()
		return battery.percent
	except PermissionError:
		return None

def IP_sistema():
	hostname = socket.gethostname()
	ip = socket.gethostbyname(hostname)
	return {"nome":hostname, "IP":ip}

	
	
	
def infor_sistema():
	carga=bateria()
	disco=armazenamento()
	ram=memoria()
	detalhes=dispositivo()
	process=cpu()
	ip=IP_sistema()
	print("ARMAZENAMENTO:")
	for chave,valor in disco.items():
		print(f"{chave}:{valor/1024**3:.2f} GB")
	print("-------------------------------------------------------------")
	print("MEMÓRIA:")
	for chave,valor in ram.items():
		print(f"{chave}:{valor/1024**3:.2f} GB")
	print("-------------------------------------------------------------")
	print("CPU:")
	for chave,valor in process.items():
		print(f"{chave}:{valor}")
	print("-------------------------------------------------------------")
	print("BATERIA:")
	if carga:
		print(f"porcentagem:{carga} %")
	else:
		print("não foi possivel obter a informação")
	print("-------------------------------------------------------------")
	print("REDE:")
	print(f"IP LOCAL: {ip["IP"]}")
	print(f"nome:{ip["nome"]}")
	print("-------------------------------------------------------------")
	print("DETALHES:")
	for chave,valor in detalhes.items():
		print(f"{chave}:{valor}")
	print(f"sistema: {platform.system()}")
	

	