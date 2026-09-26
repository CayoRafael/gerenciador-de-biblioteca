#faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior eo menor peso lidos.
tot = 0
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    print('{}'.format(peso))
    tot += 1
print('Do total de {} pessoas entrevistadas. O MAIOR PESO foi entre eles foi {} Kg e o MENOR PESO entre os entrevistados foi {} Kg '.format(tot,maior,menor))

