responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

# utilizo um for para iterar sobre o subconjunto de objetos "produtos" presente no responsejson
for j in responsejson["produtos"]:
    # se o meu iterador, encontrar um valor "Produto B" no campo "nome"
        if j["nome"] == "Produto B":
            # ele insere o valor do campo "preço" na variável resultado
            resultado = j["preço"]