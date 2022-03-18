import requests

url = 'https://viacep.com.br/ws/{}/json/'

ceps = ['04101300', '80530230', '23575460', '35460000', '13085693']

cabecalho = 'cep;logradouro;complemento;bairro;localidade;uf;ibge;gia;ddd;siafi;\n'

registros = []

registros.append(cabecalho)

for cep in ceps:
    resposta = requests.get(url.format(cep))
    if resposta.status_code == 200:
        payload = resposta.json()

        registros.append(f"{payload['cep']};"
                         f"{payload['logradouro']}; "
                         f"{payload['complemento']}; "
                         f"{payload['bairro']}; "
                         f"{payload['localidade']}; "
                         f"{payload['uf']}; "
                         f"{payload['ibge']}; "
                         f"{payload['gia']}; "
                         f"{payload['ddd']}; "
                         f"{payload['siafi']};\n ")

with open('registro.csv', 'x') as arquivo:
    arquivo.writelines(registros)
