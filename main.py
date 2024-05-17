import textwrap

def menu ():
    menu = """
\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
\n
"""
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato):
    if valor > 0 :
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n" 
    else :
        print("Operação falhou: O valor informado é invalido")  
    return saldo , extrato

def sacar(*,saldo,valor,extrato,limite,limite_saque, numeros_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numeros_saques > limite_saque

    if excedeu_saldo :
        print("Saldo insuficiente")
    elif excedeu_limite:
        print("Execedeu o valor limite para saque ")
    elif excedeu_saque:
        print("Execedeu o limite de saques diarios")
    elif valor > 0 :
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numeros_saques += 1
    else :
        print("Operação falhou : O valor informado é invalido") 

    return saldo, extrato

def exibir_extrato(saldo,/,*, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def main():
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
                exibir_extrato(saldo, extrato=extrato)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
