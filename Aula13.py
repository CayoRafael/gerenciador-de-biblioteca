for c in range(0, 6): #se quiser colocar para trás colocar (6, 0, -1) se colocar (0,7,2) ele conta pulando de 2 em 2.
    print(c)
print('FIM')
n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
print('FIM')
for n in range(1,51):
    print('.', end='')
    if n % 2 == 0:
        print(n, end='')
print('Acabou')
soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        print(c, end=' ')
        cont = cont + 1     #conta todos os valores
        soma = soma + c     #soma todos eles
print('A soma de todos {} os valores é {}'.format(cont,soma))
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num,c,num*c))
print('fim')

soma = 0
cont = 0
for c in range(1, 7):
        n = int(input('Digite um valor: '))
        if n % 2 == 1:
            soma += n
            cont += 1
print('Você informou {} valores impares e a soma deles é {}  '.format(cont, soma))