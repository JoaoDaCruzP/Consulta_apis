import requests

def consulta_clima(nome):
    url = f'https://wttr.in/{nome}?format=j1'
    resposta = requests.get(url)


    if resposta.status_code == 200:
        info = resposta.json()

        dados = info['current_condition'][0]

        print(f'A temperatura em {cidade.capitalize()} é de:' , dados['temp_C'],'Graus')
    
    else:
        print(resposta.status_code)
  

cidade = input('digite a cidade: ')

consulta_clima(cidade)