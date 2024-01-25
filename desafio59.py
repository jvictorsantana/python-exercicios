n1 = int(input('Informe o primeiro número '))
n2 = int(input('Informe o segundo número '))
opcao = 0
while opcao != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] FINALIZAR PROGRAMA''')
    opcao = int(input('>>> Qual é a sua opção? '))
    if opcao == 1:
        print(f'A soma de {n1} + {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} x {n2} = {n1*n2} ')
    elif opcao == 3:
        print(f'O maior número entre {n1} e {n2} é {max(n1, n2)}')
    elif opcao == 4:
        print('Infome novos números')
        n1 = int(input('Informe um novo número '))
        n2 = int(input('Informe mais um novo número '))

    elif opcao == 5:
        print('Programa finalizado!')
    else:
        print('Opção inválida, escolha uma opção correta!')