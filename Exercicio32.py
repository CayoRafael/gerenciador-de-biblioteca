from datetime import date
print('''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO''')
Ano = int(input('Que ano você quer analisar? coloque zero para o ano atual: '))
if Ano == 0:
    Ano = date.today().year
if Ano % 4 == 0 and 100 != 0 or Ano % 400 == 0:
    print('{} é um ano Bissexto: '.format(Ano))
else:
    print('{} não é um ano Bissexto'.format(Ano))