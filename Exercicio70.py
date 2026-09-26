'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
print('---------------------')
print('LOJÃO DOS IMPORTADOS: ')
print('---------------------')
total = totmil = menor = Valor = cont = 0
barato = ' '
while True:
    Produto = str(input('Produto: ')).strip().upper()
    Valor = float(input('Valor: R$ '))
    cont += 1
    if cont == 1 or Valor < menor:
        menor = Valor
        barato = Produto
    total += Valor
    if Valor > 1000:
        totmil += 1
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar? - [S/N]: ')).strip().upper()[0]
    if opc == 'N':
            break
print(f'O TOTAL DA COMPRA FOI {total:5.2f}R$')
print(f'UM TOTAL DE {totmil} PRODUTOS CUSTAM MAIS 1000R$.')
print(f'O PRODUTO MAIS BARATO FOI O/A {barato} E CUSTA {menor}R$')
print('{:-^40}'.format(' FIM DO PROGRAMA! '))


