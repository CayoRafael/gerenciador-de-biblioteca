#refaça o desafio 009, mostrando a tabuada de um numero que o usuário escolher, só que usando o laço for.
print('======= \033[1;34m  T A B U A D A \033[m ========')
i = int(input('\033[1;36m Digite um número: \033[m  '))
print('\033[1;32m A TABUADA DO NÚMERO {} É: \033[m '.format(i))
for c in range(1,11):
    print('\033[1;35m {} X {} = {} '.format(i,c,i*c))
print('\033[1;32m FIM')