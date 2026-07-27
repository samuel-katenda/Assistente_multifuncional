import requests
import time
import datetime


def monitorar_bitcoin(intervalo=5):
    arquivo="informações_de_monitoramento bitcoin.txt"
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    preco_anterior = None

    print("--- 🚀 MONITORANDO BITCOIN EM TEMPO REAL ---")
    tempo=0

    try:
        while True:
            try:
                
                resposta = requests.get(url, timeout=10)
                resposta.raise_for_status()

                preco_atual = float(resposta.json()["price"])
                hora = datetime.datetime.now().strftime("%H:%M:%S")
                mensagem = f"[{hora}] Bitcoin: ${preco_atual:.2f}"

                with open(arquivo, "a", encoding="utf-8") as f:
                    f.write(mensagem + "\n")

                if preco_anterior is None:
                    print(mensagem)
                    tempo+=1
                elif preco_atual > preco_anterior:
                    print(f"📈 {mensagem} (Subindo!)")
                    tempo+=1
                elif preco_atual < preco_anterior:
                    print(f"📉 {mensagem} (Caindo!)")
                    tempo+=1
                else:
                    print(f"➡️ {mensagem} (Sem alteração)")
                    tempo+=1

                preco_anterior = preco_atual

            except Exception as erro:
                print(f"Erro: {erro}")
                tempo+=1

            time.sleep(intervalo)
            if tempo>10:
            	print("terminado o monitoramento...")
            	break

    except KeyboardInterrupt:
        print("\n--- 🛑 Monitoramento encerrado pelo usuário. ---")
        
        
