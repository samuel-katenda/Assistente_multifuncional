import requests
import key_api as chave

def estado_tempo(cidade=None):
    if not cidade:
        return False

    api_key=chave.chave_clima()

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    )

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()

        dados = resposta.json()

        print(f"Cidade: {dados['name']}")
        print(f"Temperatura: {dados['main']['temp']}°C")
        print(f"Clima: {dados['weather'][0]['description']}")
        print(f"Umidade: {dados['main']['humidity']}%")

    except requests.exceptions.ConnectionError:
        print("Erro: sem ligação à Internet.")

    except requests.exceptions.Timeout:
        print("Erro: o servidor demorou demasiado para responder.")

    except requests.exceptions.HTTPError:
        print("Erro: cidade inválida ou problema na API.")

    except requests.exceptions.RequestException as erro:
        print(f"Erro inesperado: {erro}")
        
        
        