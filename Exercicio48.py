#faça um programa que calcule a soma entre todos os números
#impares que são multiplos de três e que se encontram no intervalo de 1 até 500.
i = 3
f = 500
p = 6
s = 0
cont = 0
for c in range(i,f,p):
    print(c)
    s += c #pode ser soma = c + 1
    cont = cont +1 #pode ser cont += 1
print('O somátório de todos os {} valores foi impares foi {} '.format(cont,s))
