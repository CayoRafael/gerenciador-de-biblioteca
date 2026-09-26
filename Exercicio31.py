import emoji
print("""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem:
Cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas. """)
print(emoji.emojize(':bus:-----PREÇO----DA---PASSAGEM------:bus:'))
Distancia = float(input(emoji.emojize('Qual a distancia em quilometros de sua viagem: :oncoming_automobile: ')))
if Distancia < 200:
    print('O valor da sua passagem é {}'.format(Distancia*0.5))
else:
    print('O valor da sua passagem é: {}'.format(Distancia*0.45))
