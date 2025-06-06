import requests

def busca_pais(nome):
    url = f"https://restcountries.com/v3.1/name/{nome}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados  = resposta.json()
        pais = dados[0]
    
        print('informações encontradas:')
        print('nome',pais["name"]["common"])
        print('Capital do pais é:',pais["capital"][0])
        print("Bandeira:", pais["flags"]["png"])

    else:
        print('pais nao encotrado ou erro de api')

pais = input('digite o nome do pais: ')

busca_pais(pais)
