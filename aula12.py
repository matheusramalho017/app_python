import requests

def retorna_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.text)
    dados_cep = response.json()
    print (dados_cep['complemento'])
    print(dados_cep['logradouro'])
    print(dados_cep['bairro'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

if __name__ == '__main__':
    dados_pokemon = retorna_dados_pokemon('charizard')
    print(dados_pokemon)
    # retorna_cep('01001000')
