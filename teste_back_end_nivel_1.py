#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TESTE DE BACKEND NIVEL 1 - GRUPO PEGAZUS

#Faça o teste abaixo 100% sozinho, sem a ajuda de CHAT GPT, amigos, familiares, professores ou etc.. conseguimos facilmente identificar

#lembre-se de detalhar as respostas, assim conseguimos analisar ainda mais o seu conhecimento tecnico

#caso prefira, pode fazer o desafio em outro arquivo separado, e só colar a solução completa abaixo de cada exercicio
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
#Explique detalhadamente por que voce decidiu essa solução e não outra
response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]
# criando um novo array para passar o resultado
resultado = [
    j
    # utilizo a lógica de um for encadeado, primeiro para passar por cada objeto em response
    for i in response
    # segundo para passar por cada "produto" dentro de cada objeto
    for j in i["produtos"]
    # se o preço do produto for maior ou igual a 30, ele será adicionado no array resultado
    if j["preço"] >= 30
]


#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

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
# escolhi esta opção por ser simples e de forma rápida iterar sobre os elementos de responsejson


#3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]
for i in range(len(lista)):
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux
# como se trata de uma lista númerica simples, utilizei o algoritmo bubbleSort onde a cada iteração
# é verificado se o valor à frente é menor, se sim, as posições são trocadas

#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela

lista = ["   joao   ","   maria   ","  joana  "]
listaB = []
for i in range(len(lista)):
    listaB.append(lista[i].strip())
print(listaB)

#5-Retire o segundo item dessa lista e imprima ela:

lista = [1,2,3,4,5,6]
lista.pop(1)
print(lista)

#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]
lista = ["maria" if x == "joao" else x for x in lista ]

#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra
count = 0
lista = [0, 1, 2, 3, 4, 5]
while count < len(lista):
    if lista[count] <= 5:
        print(lista[count])
        lista[count] = lista[count] + 1
    count += 1
# decidi utilizar esta solução pois me permite ter mais controle sobre o código através da variável count

#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra
import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos")
result = response.json()
def func(result):
    countCompleted = 0;
    countPending = 0
    for i in result:
        if i['completed'] == True:
            countCompleted += 1
        else:
            countPending += 1
    return countCompleted, countPending
completed, pending = func(result)
# achei mais elegante criar a função para tratar apenas a query solicitada no Json, sem encapsula-lo dentro do escolpo
# da função, possibilitando assim a utilização da variavel result em outras querys

#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra
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
# Nesta abordagem eu inicializei uma lista vazia e no loop for, iterei sobre o result contendo o json e, dentro do append
# ja realizei o parser de forma direta, uma maneira rápida, simples e eficaz

#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO
fila = []
fila.append(1)
fila.append(2)
fila.append(3)
fila.pop(0)

#11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO
pilha = []
pilha.append('joca')
pilha.append('carlos')
pilha.append('josé')
pilha.pop()

#DESAFIO!!

#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta

class Conta:
    contId = 1
    def __init__(self, nome, cpf):
        self.id = Conta.contId
        Conta.contId += 1
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
    def sacar(self, valor):
        if (valor > 0 and valor <= self.saldo):
            self.saldo -= valor
        else:
            print("Operação impossível, saldo insuficiente")

    def deposito (self, valor):
        if (valor > 0):
            self.saldo += valor
        else:
            print("O valor do depósito deve ser positivo")

    def mostrarSaldo(self):
        print(f"R$ {self.saldo:.2f}")

conta_atual = None

def criar_conta():
    nome = input("Informe o nome do cliente: ")
    cpf = input("Informe o CPF do cliente: ")
    conta = Conta(nome, cpf)
    print(f"Conta criada com sucesso! ID da conta: {conta.id}")
    return conta

while True:
    print("\nBem-vindo ao Banco! Escolha uma operação:")
    print("1. Criar conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Consultar saldo")
    print("5. Sair")
    op = input("Escolha uma opção: ")

    if op == '1':
        conta_atual = criar_conta()

    elif op == '2':
        valor = float(input("Informe o valor a ser depositado: R$"))
        conta_atual.deposito(valor)

    elif op == '3':
        valor = float(input("Informe o valor de saque: R$"))
        conta_atual.sacar(valor)

    elif op == '4':
        conta_atual.mostrarSaldo()

    elif op == '5':
        print("Saindo da conta, obrigado e até a próxima!")
        break

    else:
        print("Opção inválida. Tente novamente")







