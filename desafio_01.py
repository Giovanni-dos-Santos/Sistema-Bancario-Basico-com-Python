saldo = 0.0
limite_maximo_saque = 500.0
extrato = ""
numero_saques = 0
LIMITE_DIARIO_SAQUE = 3

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Digite o valor a ser depositado: "))
        if deposito <= 0.0:
            print("Por favor, digite um valor válido.")
        else:
            saldo += deposito
            extrato += f"Deposito: R${deposito:.2f}\n"
            print("Valor depositado com sucesso!\n")

    elif opcao == "2":
        saque = float(input("Digite o valor a ser sacado: "))
        if saque <= 0.0:
            print("Por favor, digite um valor válido.")
        elif saque > limite_maximo_saque:
            print("Você excedeu o limite de R$500 por saque. Escolha outro valor.")
        elif numero_saques >= LIMITE_DIARIO_SAQUE:
            print("Você excedeu o limite diário de saques. Tente novamente mais tarde.")
        elif saldo > saque:
            print("Saldo insuficiente para realizar o saque.")
        else:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque: R${saque:.2f}\n"
            print("Valor saquado com sucesso!\n")

    elif opcao == "3":
        print("\nEXTRATO".center(11,"-"))
        if extrato:
            print(extrato)
        else: 
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo atual: R${saldo:.2f}")

    elif opcao == "0":
        break

    else:
        print("\nPor favor, digite uma das opções válidas.")

    