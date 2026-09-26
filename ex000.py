N1 = int (input ('Escreva um valor: '))
N2 = int (input ('Escreva outro valor: '))
S = N1 + N2
M = N1 + N2
D = N1 / N2
DI = N1 // N2
E = N1 ** N2
print ('A soma é {}, o produto é {} e a divisão é {:.3f}'.format (S,M,D), end='')
print ('A divisão inteira é {}, e a exponenciação é {} '.format (DI,E))