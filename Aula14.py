'''for c in range(1,10):
    print(c)'''
'''c = 1
while c <10:
    print(c)
    c += 1 #lembre c = c +1 é a mesma coisa.
print('Fim')'''
'''n = 1
while n != 0:  #condição de parada 'flag'
    n = int(input('Digite um valor: '))
print('fim')'''
'''r = 'S'
while r == 'S':  #condição de parada 'flag'
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('fim')'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} valores pares e {} valores impares!'.format(par,impar))

print('Acabou')


