# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto:
# Em até 2x no cartao: preço normal
# 3x ou mais no cartão: 20% de juros
print('='*20,'LOJAS JOÃO VICTOR','='*20)
preco = float(input('Informe o preço do produto: '))
forma_de_pagamento = int(input('-=-= Escolha a forma de pagamento =-=-\n1) À vista\n2) Débito\n3) Em até 2x no cartão\n4) 3x ou mais no cartão\n -- '))
if forma_de_pagamento == 1:
    print(f'Você ganhou 10% de desconto, você pagará R${preco*(1-0.1):.2f}')
elif forma_de_pagamento == 2:
    print(f'Você ganhou 5% de desconto, você pagará R${preco*(1-0.05):.2f}')
elif forma_de_pagamento == 3:
    print(f'Você poderá parcelar sua compra em até 2x vezes sem juros!')
else:
    print(f'Para parcelar em mais de 3 no cartão ficará um acréscimo de 20% sobre o valor total da compra, você pagará R${preco*(1+0.2):.2f}')        

#Resolução do professor
prec = int(input('Preço das compras: R$'))
print(''' FORMA DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = prec - (prec * 10/100)
elif opcao == 2:
    total = prec - (prec * 5/100)    
elif opcao == 3:
    total = prec
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
    print(f'Sua compra de {prec:.2f} vai custar {total:.2f}')
elif opcao == 4:
    total = prec + (prec * 20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f}')    
    print(f'Você pagará um total de R${total:.2f}')