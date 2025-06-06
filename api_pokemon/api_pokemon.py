import requests
from time import sleep

def carregando():
    print('aguarde',end='')
    for i in range(4):   
        print('.',end='',flush=True)
        sleep(1)
    print('')

def busca_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}" #endereço da api
    resposta = requests.get(url) #faz um get(pega) da API e salva na variavel


    if resposta.status_code == 200: #faz um tratamento de erro onde 200 é Sucesso

        dados_encontrados = resposta.json() #precisa tratar os dados e salvar como JSON

        carregando()
      
        print('nome:',dados_encontrados["name"].upper())
        print('altura: ',dados_encontrados['height'])
        print('esse pokemon pesa: ',dados_encontrados['weight'])

        
        print('Imagem: ',dados_encontrados['sprites']['front_default'])

    else:
        print('pokemon nao encontrado ou erro de API')




nome  = input('Digite o nome do pokemon: ')

busca_pokemon(nome)