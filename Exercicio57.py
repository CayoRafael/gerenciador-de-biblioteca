''' Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado,
peça a digitação novamente até ter um valor correto.'''
Mas = 'M'
Fem = 'F'
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
while sexo != Mas and sexo != Fem:
    sexo = str(input('Dado invalido.Por favor, informe seu sexo [M/F]: ')).strip().upper()
if sexo == Mas:
    resultado = 'Masculino'
else:
    resultado = 'Feminino'
print('Sexo registrado com sucesso o sexo escolhido é o {}'.format(resultado))
#Resolução de guanabara
#sexo str(input('informe seu sexo: [M/F]').strip().upper()[0]
#while sexo not in 'MmFf':
#   Sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
#print('Sexo {} registrado com sucesso'.format(sexo))




