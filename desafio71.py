# Crie um programa que simule o funcionamento de um caixa eletronico. No início, pergunte ao usuário qual 
# será o valor sacado (n inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# obs: Considere que o caixa possui cédulas de R$50,00, R%20,00, R$10,00, R$1,00

print('-=-'*13)
print(f'{'-'*10} BANCO COMERCIAL JV {'-'*10}')
print('-=-'*13)
print('Notas Disponíveis:\n\n- R$50,00\n- R$20,00\n- R$10,00\n- R$1,00\n')
saque = int(input('Quanto deseja sacar? '))
caixa = saque
ced = 50
notas = 0
while True:
    if caixa >= ced:
        caixa-= ced
        notas += 1
    else:
        if notas > 0:
            print(f'Total de {notas} cédulas de R${ced}')
        
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
                notas = 0
            if caixa == 0:    
                break    
    

           

        
    
print(f'Saque efetuado com sucesso!')     
