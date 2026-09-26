print('''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.''')
N1 = int(input('Primeiro  número: '))
N2 = int(input('Segundo número: '))
N3 = int(input('Terceiro número: '))
if N1 > N2 and N1 > N3:
    Maior = N1
if N2 > N1 and N2 > N3:
    Maior = N2
if N3 > N1 and N3 > N2:
    Maior = N3
if N1 < N2 and N1 < N3:
    Menor = N1
if N2 < N1 and N2 < N3:
    Menor = N2
if N3  < N1 and N3 < N2:
    Menor = N3
print('O maior número é: {} '.format(Maior))
print('O menor número é: {}  '.format(Menor))
