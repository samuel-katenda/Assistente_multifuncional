from google import genai
from key_api import chave_ia
import httpx

def sistema_ia(pergunta):
    try:
        chave_token = chave_ia()
        client = genai.Client(api_key=chave_token)
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=pergunta
        )
        return response.text

    except httpx.ConnectError:
        return "Erro, verifica o teu acesso à internet"
    except httpx.ReadTimeout:
    	return "O servidor demorou demasiado"
    except Exception as e:
    	return f"Ocorreu um erro: {e}"
