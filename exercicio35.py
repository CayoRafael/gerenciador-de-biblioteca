print('''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.''')
print("==="*40)
print('ANALISADOR DE TRIANGULOS')
print("==="*40)
S1 = float(input('Digite um valor p/ PRIMEIRO SEGUIMENTO:  '))
S2 = float(input('Digite outro valor p/ SEGUNDO SEGUIMENTO:  '))
S3 = float(input('Digite mais um valor p/ TERCEIRO SEGUIMENTO: '))
if S1<S2+S3 and S3<S1+S2 and S2<S1+S3:
    print('ESTES SEGUIMENTOS PODEM FORMAR UM TRIANGULO: ')
else:
    print('OS SEGUIMENTOS ACIMA NÃO FORMAM UM TRIANGULO: ')