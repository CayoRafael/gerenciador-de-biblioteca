#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.# \(an = a_1 + (n - 1) . r
Primeiro = int(input('Digite o primeiro termo: '))
Razão = int(input('Digite a Razão: '))
Décimo = Primeiro + (10 - 1 ) * Razão
for c in range(Primeiro,Décimo + Razão,Razão):
    print('{}'.format(c), end=' ↦ ')
print('Acabou')