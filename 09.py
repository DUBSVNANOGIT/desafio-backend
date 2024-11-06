import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")
result = response.json()
def func(result):
    dados = []
    for i in result:
        dados.append({
            'nome':i['name'],
            'username': i['username'],
            'email': i['email'],
            'rua': i['address']['street'],
            'numero': i['address']['suite']
        })
    return dados

