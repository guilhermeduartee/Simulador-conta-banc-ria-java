menu = """
"===============================================================")
Olá, seja bem-vindo(a) ao seu banco virtual
Selecione uma opção baixo para a ação que você deseja tomar:

DEPOSITAR (D)
SACAR     (S)
EXTRATO   (E)
SAIR      (Q)


===========================================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido")


    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Erro: Você não possui saldo sulficiente! ")

        elif excedeu_limite:
            print("Erro: Você execeu o seu limite! ")

        elif excedeu_saques:
            print("Erro: Você excedeu o seu limite de saques diários! ")

        if valor > saldo:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("Saldo insuficiente para saque")
    
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações na sua conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

