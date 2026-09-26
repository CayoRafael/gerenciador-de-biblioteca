from random import randint
from time import sleep
'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
print('=-=-=-= JOGO DE PAR OU IMPAR =-=-=-=')
print('SE VOCÊ DESEJA PAR DIGITE - [0]')
print('SE VOCÊ DESEJA IMPAR DIGITE - [1]')
n = 0
cont = 0
while True:
    esc = int(input('VOCE ESCOLHE: - [PAR] ou [IMPAR]: '))
    if esc == 1:
        print(f'VOCÊ ESCOLHEU IMPAR! SEU ADVERSÁRIO É PAR.')
    elif esc == 0:
        print(f'VOCÊ ESCOLHEU PAR SEU ADVERSÁRIO É IMPAR!')         #tipo = ' '
    else:                                                           #while tipo not in 'PpIi':
        print('Jogada inválida!')                                   #tipo = str(input('Par ou Impar').strip().upper()[0]
        esc = int(input('Digite sua escolha novamente: - [PAR] ou [IMPAR]: '))
    n = int(input('\033[1mEscolha seu número entre 1️ e 1️0:\033[m '))
    sleep(1)
    itens = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    pc = randint(1, 10)
    print(f'Voce escolheu o número: {n} e o seu adversário o número: {pc}')
    soma = (pc + n)
    res = soma %2
    cont +=1
    if res == esc:
        print(f'\033[1;32mVOCÊ VENCEU!\033[m✅ ', end='')
        print('DEU PAR!' if res == 0 else 'DEU IMPAR!')
        print('\033[1mVamos jogar denovo\033[m❔')
    elif res != esc:
        print(f'\033[1;31mVOCÊ PERDEU!\033[m❌ ', end='')
        cont -= 1
        print('DEU PAR!' if res == 0 else 'DEU IMPAR!')
        print(f'Você jogou {cont+1} partidas e teve {cont} vitórias consectivas')
        break
print('FIM DO PROGRAMA')








