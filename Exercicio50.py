#desenvolva um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares.
# se o valor digitado forimpar desconsidere-o.
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0: #se mudar o resto pra 1 da valores impares.
        soma += num
        cont += 1
print('Você informou {} números PARES e a SOMA foi {}'.format(cont,soma))





