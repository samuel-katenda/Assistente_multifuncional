import subprocess , psutil , platform



def abrir_programa(prog=None):
    if not prog:
        return None

    try:
        if prog in programas:
            subprocess.Popen([programas[prog]])
        else:
            if not prog.lower().endswith(".exe"):
                prog += ".exe"

            subprocess.Popen([prog])

        return True

    except (FileNotFoundError, PermissionError, OSError):
        return None
		
programas = {
    "bloco de notas": "notepad",
    "paint": "mspaint",
    "calculadora": "calc",
    "cmd": "cmd",
    "powershell": "powershell",
    "terminal": "wt",
    "explorador": "explorer",
    "gerenciador de tarefas": "taskmgr",
    "registro": "regedit",
    "configurações": "ms-settings:",
    "painel de controle": "control",
    "chorme": r"C:\Program Files\Google\Chrome\Application\chrome.exe","Word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "Excel":r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"}
    
def listar_processos():
    for pid in psutil.pids():
        try:
        	processo = psutil.Process(pid)
        	print(pid, processo.name())
        except psutil.NoSuchProcess:
        	pass

def fechar_programa(nome=None):
	if not nome:
		return None
	for processo in psutil.process_iter(["pid","name"]):
		if processo.info["name"]==nome.lower():
			processo.terminate()
			return True
		return None
	
def desligar_sistema():
	try:
		sistema=platform.system()
		if sistema=="Windows":
			subprocess.run(["shutdown", "/s","/t", "0"],check=True)
		elif sistema=="Linux":
			subprocess.run(["systemctl","poweroff"],check=True)
		elif sistema=="Darwin":
			subprocess.run(["shutdown","-h","now"],check=True)
		else:
			return None
	except (subprocess.CalledProcessError,FileNotFoundError,PermissionError):
		return None

def reiniciar_sistema():
    sistema = platform.system()

    try:
        if sistema == "Windows":
            subprocess.run(["shutdown", "/r", "/t", "0"], check=True)
        elif sistema in ("Linux", "Darwin"):
            subprocess.run(["sudo", "reboot"], check=True)
        else:
            return False

        return True

    except (FileNotFoundError, PermissionError, subprocess.CalledProcessError):
        return False
	
	

	