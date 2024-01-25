# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá 
# perguntar se o usuário quer ou nao continuar. No final, mostre:
# A - Quantas pessoas tem mais de 18 anos
# B - Quantos homens foram cadastrados
# C - Quantas mulheres tem menos de 20 anos

cont_idade = 0
cont_masculino = 0
cont_feminino = 0
while True:
    idade = 0
    sexo = ''
    s = ''
    n = ''
    print('-'*25)
    pergunta = input('Quer Cadastrar? [S/N] ').lower().strip()
    print('-'*25)
    if pergunta == 'n':
        break
    else:
        while s != 'm' and s != 'f':
            s = input('Infome o seu sexo: [M/F] ').lower().strip()
        n = int(input('Qual a sua idade: '))
        idade += n
        if idade > 18:
            cont_idade += 1
        if s == 'm': 
            cont_masculino += 1
        if s == 'f' and n < 20:
            cont_feminino += 1

print('-=-'*20)
print(' '*20,'CADASTRO DE PESSOAS!',' '*20)
print('-=-'*20)
print(f'Foram cadastradas {cont_idade} pessoas com idade acima dos 18 anos')  
print(f'Foram cadastrados {cont_masculino} homens!')  
print(f'Foram cadastradas {cont_feminino} mulheres com menos de 20 anos')
    