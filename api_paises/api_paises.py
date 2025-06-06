#passo 01 - importar a biblioteca que trata os url chamada requests

import requests

#passo 02 - fazemos uma função com o objetivo de pegar as informacoes da api e salvar como resposta o resultado

def busca_pais(nome):
    url = f"https://restcountries.com/v3.1/name/{nome}"

    resposta = requests.get(url)

    #passo 03 - desenvolvemos as condicões de tratamento do conteudo obtido na variavel resposta

    if resposta.status_code == 200:
        dados = resposta.json()
        pais = dados[0]
        moeda = list(pais["currencies"].keys())[0]

    #passo 04 - imprimimos que desejamos saber sobre os dados tratados
        print("Informações encontradas:")
        print("Nome:", pais["name"]["common"])
        print("Capital:", pais["capital"][0])
        print("População:", pais["population"])

        moeda = list(pais["currencies"].keys())[0]
        simbolo = pais["currencies"][moeda]["symbol"]
        print("Moeda:", moeda, "-", simbolo)
        print("Bandeira:", pais["flags"]["png"])

    else:
        print('pais nao encontrado ou erro de api')
    
pais = input('qual o nome do pais desejado?: ')

#passo 05 - finalmente chamamos a função para obter o resultado esperado
busca_pais(pais)