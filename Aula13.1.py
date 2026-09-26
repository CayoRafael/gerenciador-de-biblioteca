i = int(input('inicio '))
f = int(input('Fim '))
p = int(input('Passo '))
for c in range(i, f+1,p):
    print(c)
print('FIM')
s = 0
for c in range(0,3):
    n = int(input('Digite um valor: '))      #vai pedir pra dar valores quantas vezes colocar ali no range
    s += n
print('O somátório de todos os valores foi {} '.format(s))