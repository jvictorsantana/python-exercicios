#Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar
# o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
prazo = int(input('Quantos anos vai pagar a casa? '))
prestacao_mensal = valor_casa/(prazo * 12)/0.3

if prestacao_mensal <= salario:
    print()
    print(f'NEGÓCIO FECHADO!\nVocê vai pagar parcelas de R${prestacao_mensal * 0.3:.2f} por mês!')
else:
    print()
    print(f'Você não se enquadra nas condições, a prestação mensal de R${prestacao_mensal * 0.3:.2f} excedeu 30% do seu salário!\nFaça uma nova simulação, a parcela máxima permitida é de R${salario * 0.3:.2f}')

# Resolução do Professor
    
casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos ', end='')
print(f'a prestação será de {prestacao:.2f}')
if prestacao<=minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')    