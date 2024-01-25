
# Faça um programa que mostre a tabuada de varios números, 1 de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.  

while True:
    n = int(input('Escolha o número para a tabuada: '))
    print('-=-'*6)

    if n < 0:
        print('Número negativo não será contabilizado. Programa finalizado!')
        break
    else:
        print('')
        print(f'A tabuada do {n} é:')
        for c in range(1, 11):
            print(f'{n} x {c} = {n*c}')
        
