import requests as rq

def busca_moeda(nome):
    url = f'https://economia.awesomeapi.com.br/json/last/{nome}'
    resposta = rq.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = nome.replace("-", "")  # Ex: USD-BRL → USDBRL
        if chave in dados:
            info = dados[chave]
            print('Deu certo!')
            print(f"Cotação {info['name']}: R$ {info['bid']}")
        else:
            print('Moeda não encontrada. Verifique o formato (ex: USD-BRL).')
    else:
        print('Erro ao acessar a API.')

moeda = input('Digite a moeda no formato "USD-BRL", "EUR-BRL", etc.: ')
busca_moeda(moeda.upper())
