# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
# A - Qual é o total gasto de compra 
# B - Quantos produtos custam mais de 1.000 reais
# C - Qual o nome do produto mais barato

total = 0
cont_mil = 0
p_barato = ''
cont = 0
menor = 0
print('-=-'*10)
print(f'{'-'*10} LOJAS JV {'-'*10}')
print('-=-'*10)
while True:
    p = input('Deseja Solicitar algum produto? [S/N] ').upper().strip()
    print('')
    cont += 1
    if p == 'S':
        produto = input('Informe o nome do produto: ').upper().strip()
        valor = float(input('Quanto custa o produto: '))
  
        if valor > 1000:
            cont_mil += 1

        if cont == 1 or valor < menor:
            menor = valor
            p_barato = produto
        else:        
            if valor < menor:
                menor = valor
                p_barato = produto

        total += valor    
    if p == 'N':
        break
print(f'{'-'*5} Obrigado por visitar a nossa loja! {'-'*5}\n\nO valor total da sua compra foi: R${total:.2f}\n\nVocê comprou {cont_mil} produtos acima de mil reais\n\nO produto de menor valor foi o(a) {p_barato}, custando R${menor:.2f}')    

    