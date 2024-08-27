menu = '''

[d] Depósito
[s] Saque
[e] Extrato
[x] Sair

'''

saldo = 0
limite_saque = 500
extrato = ''
numero_saques = 0
LIMITE_DIARIO = 3


while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Quanto você quer depositar? "))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print("Operação inválida. Informe um valor válido")
        

    elif opcao == 's':
        valor = float(input())
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saque = numero_saques >= LIMITE_DIARIO

        if excedeu_saldo:
            print('Valor do saque maior do que saldo atual')
        elif excedeu_limite:
            print('Valor do saque maior do que o limite permitido')
        elif excedeu_saque:
            print('Limite diário de saques execedido, tente novamente amanhã')
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f'Saque: R$ {valor:.2f}\n'
        else:
            print('Operação inválida')

    elif opcao == 'e':
        print(f'\n******************** EXTRATO ********************')
        print('Sem nenhuma movimentação' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('*************************************************')

    elif opcao == 'x':
        print("saindo")
        break

    else:
        print('Opção inválida')


