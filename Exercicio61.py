'''Refaça o desafio 051 lendo o primeiro termo e a razão de P.A,
mostrando os 10 primeiros termos da progressão usando a estrutura while '''
print('=-='*20)
termo = int(input('\033[1;33m Qual o primeiro termo da P.A? '))
print('=-='*20)
razao = int(input('\033[1;32m Qual a razão desta P.A '))
print('=-='*20)
cont = 1
while cont <= 10:
    print('\033[1;33m a{}\033[1;32m = \033[m {},'.format(cont, termo), end='')
    #  print(f' o {termo} → ', end='') mesma coisa
    termo += razao
    cont += 1
print('  \033[1;32mFIM \033[1;33mDA \033[1;32mP.A     ')




