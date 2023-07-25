saldo = 0
depositos = []
saques = []


def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        depositos.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Erro: O valor do depósito deve ser positivo.")


def sacar(valor):
    global saldo
    if valor > 0 and valor <= 500 and len(saques) < 3:
        if saldo >= valor:
            saldo -= valor
            saques.append(valor)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Erro: Saldo insuficiente para realizar o saque.")
    else:
        print("Erro: Valor de saque inválido ou limite diário de saques atingido.")


def extrato():
    if not depositos and not saques:
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato de movimentações:")
        for deposito in depositos:
            print(f"Depósito: R$ {deposito:.2f}")
        for saque in saques:
            print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")


while True:
    print("\nOpções:")
    print("D - Depósito")
    print("S - Saque")
    print("E - Extrato")
    print("Q - Sair")

    opcao = input(
        "Escolha a operação desejada entre as opções acima: ").lower()

    if opcao == "d":
        valor = float(input("Qual o valor que você deseja depositar? "))
        depositar(valor)
    elif opcao == "s":
        valor = float(input("Qual o valor que você deseja sacar? "))
        sacar(valor)
    elif opcao == "e":
        print("**********Extrato**********")
        extrato()
    elif opcao == "q":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida, tente outra vez.")
