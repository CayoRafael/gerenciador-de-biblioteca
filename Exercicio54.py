#crie um programa que leia o ano de nascimento de sete pessoas.
# No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
Atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(0,7):
    Nome = str(input('Digite um nome: ')).strip().upper()
    Nascimento = int(input('Em que ano você Nasceu: '))
    if Atual - Nascimento > 18:
        print('Você tem {} anos, Logo é  MAIOR DE IDADE! {}'.format(Atual-Nascimento,Nome))
        totmaior += 1
    else:
        print('Você tem {} anos, Logo é MENOR DE IDADE! {} '.format(Atual-Nascimento,Nome))
        totmenor += 1
print('Ao todo obtivemos {} pessoas maiores e {} pessoas menores. '.format(totmaior,totmenor))


