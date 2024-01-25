#Escreva um programa que pergunta o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual o seu salário? '))
if salario > 1250:
    print(f'Você recebeu um aumento de R${salario * 10/100:.2f}, o seu novo salário é de R${salario * (1+0.1):.2f} ')
else:
    print(f'Você recebeu um aumento de R${salario*15/100:.2f}, o seu novo salário é de R${salario * (1+0.15):.2f}')    