import requests
from key_api import chave_cambio

def cambio(moeda):
    chave_key=chave_cambio()
    url = f"https://v6.exchangerate-api.com/v6/{chave_key}/latest/{moeda}"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        taxas = dados["conversion_rates"]

        codigos = {
            "USD": "🇺🇸",
            "EUR": "🇪🇺",
            "GBP": "🇬🇧",
            "JPY": "🇯🇵",
            "CNY": "🇨🇳",
            "CAD": "🇨🇦",
            "AUD": "🇦🇺",
            "CHF": "🇨🇭",
            "BRL": "🇧🇷",
            "INR": "🇮🇳",
            "AOA": "🇦🇴"
        }

        for moeda_codigo, bandeira in codigos.items():
            print(f"1 {moeda} = {taxas[moeda_codigo]} {moeda_codigo} {bandeira}")

    else:
        print("Não foi possível obter a conversão")

