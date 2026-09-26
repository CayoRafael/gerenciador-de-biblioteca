'''Melhore o DESAFIO 61,
perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''
print('GERADOR DE PROGRESSÃO ARITIMÉTICA')
termo = int(input(' Qual o primeiro termo da P.A? '))
razao = int(input(' Qual a razão desta P.A? '))
cont = 1
quant = int(input(' Quantos termos você deseja? '))
adicionar = 1
while cont <= quant:
    print(' a{} = {} '.format(cont, termo), end=',' if cont < quant else'')
    #  print(f' o {termo} → ', end='') mesma coisa
    termo += razao
    cont += 1
    if cont > quant:
        print('', end='\n')
        adicionar = int(input('Quantos termos vamos adicionar? '))
        quant += adicionar
print('', end='\n')
print(f' A P.A FINALIZADA COM {quant} TERMOS MOSTRADOS ')
print('=-='*20)
print('  FIM DA PROGRESSÃO ARITIMÉTICA     ')

