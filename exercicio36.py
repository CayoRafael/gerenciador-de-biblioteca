import math,emoji
print('''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.''')
print('\033[1;33m---------\033[m'*15)
print(emoji.emojize(':yellow_circle: :green_circle: :blue_circle: \033[1;mBanco do Brasil Empréstimos :yellow_circle: :green_circle: :blue_circle:'))
print('\033[1;34m---------\033[m'*15)
E = float(input('\033[1;33m Qual valor do empréstimo  em R$ para adquirir o imóvel:  '))
P = float(input('\033[1;34m Quantos mêses de prazo você deseja: '))
S = float(input('\033[1;m Qual seu salário? '))
print(emoji.emojize('\033[1;30mA :bank: NOSSA TAXA DE JUROS É 10%'))
VEM = E*10/100+E
PM = VEM/P
Limite = S*30/100
if PM <= Limite:
   print (emoji.emojize('\033[1;mPARABÉNS VOCÊ CONSEGUIU UM EMPRÉSTIMO NO VALOR DE {} REAIS E SUA PARCELA MENSAL FICOU POR APENAS {:.2f} :money_bag: PARA COMPRAR SEU APARTAMENTO: :check_mark_button: :clapping_hands:'.format(E,PM)))
else:
    print(emoji.emojize('\033[1;mINFELIZMENTE VOCÊ NÃO POSSUI RENDA SUFICIENTE PARA REALIZAR ESSE EMPRÉSTIMO :cross_mark: Sinto Muito! :confused_face:'))
print('\033[1;33m---------\033[m' * 15)
print(emoji.emojize(':yellow_circle: :green_circle: :blue_circle: \033[1;m O Banco do Brasil agradece por sua escolha!  :yellow_circle: :green_circle: :blue_circle:'))
print('\033[1;34m---------\033[m'*15)

