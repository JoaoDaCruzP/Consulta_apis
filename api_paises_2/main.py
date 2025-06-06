import requests

def busca_pais(nome):
    url = f'https://restcountries.com/v3.1/translation/{nome}'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()[0]
        print('sucesso')

        moeda = list(dados['currencies'].keys())[0]
        simbolo_moeda = dados['currencies'][moeda]['symbol']
        nome_moeda = dados['currencies'][moeda]['name']


        print('Nome:', dados['name']['common'])
        print('Capital:', dados['capital'][0])
        print('Moeda: ', simbolo_moeda, '', nome_moeda)
        
        

    else:
        print('erro de api ou nome do pais')

pais = input('Digite o pais: ')

busca_pais(pais)