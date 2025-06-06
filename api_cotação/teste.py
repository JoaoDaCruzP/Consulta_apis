import requests

def cotacao(nome):

    url = f'https://economia.awesomeapi.com.br/json/last/{nome}'
    
    resposta = requests.get(url)

    chave = nome.replace('-','')

    if resposta.status_code == 200:
        info = resposta.json()
        dados = info[chave]

        print('moeda:',dados['name'])


    else:
        print('erro de acesso a api')


moeda = input('digite a moeda: ').upper() + '-BRL'


cotacao(moeda)
print(moeda)