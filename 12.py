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