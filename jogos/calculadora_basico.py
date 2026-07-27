
def calculadora(operacao,valor1,valor2):
	try:
		calculo=None
		match operacao:
			case "+":
				calculo=valor1+valor2
			case "-":
				calculo=valor1-valor2
			case "×":
				calculo=valor1*valor1
			case "÷":
				if valor1==0:
					return None
				calculo=valor1/valor2
			case _:
				return None
		return calculo
	except ValueError:
		return None
	