#faça um programa que leia um número inteiro e diga se ele é ou não número primo.
N1 = int(input('Digite um número: '))
tot = 0
for c in range(1, N1 + 1):
    if N1 % c == 0:
        print('\033[31m',end=' ')
        tot += 1
    else:
        print('\033[m',end=' ')
    print('{}'.format(c),end=' ')
print('')
print('\033[m O número \033[31m {} \033[m foi divisivel \033[31m{} \033[m vezes: '.format(N1, tot))
if tot == 2:
    print('\033[m Por isso ele é \033[34m PRIMO!')
else:
    print('\033[m Por isso ele \033[34m NÃO É PRIMO!')