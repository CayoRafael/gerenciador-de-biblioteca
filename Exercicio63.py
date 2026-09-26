''' Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma
Sequência de Fibonacci.
Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8'''
print('=-='*20)
print('DESCOBRINDO A SEQUÊCIA DE FIBONACCI:')
print('=-='*20)
N1 = int(input('QUANTOS TERMOS DESEJA MOSTRAR? '))
A = 0
B = 1
print(f'{A}-{B}',end='')
cont = 3    #como já temos os dois primeiros começa em 3
while cont <= N1:
    C = A + B          #Calcula o próximo da fila
    print(f'-{C}',end='')  #imprime o valor de C
    A = B              # A da um passo a frente e assume o valor de B
    B = C              # B agora da um passo a frente e assume o valor de C
    cont += 1
print('', end='\n')
print('=-='*20)
print('FIM DA SEQUÊNCIA!')


