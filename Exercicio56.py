#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo,
#qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
Somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ' '
totmulher20 = 0
for c in range(1,5):
    print('==== {}ª PESSOA ====='.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    Somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = Somaidade / 4
print('A média de idade do grupo é {} anos '.format(mediaidade))
print('O nome do homem mais velho do grupo é: {} que tem {} anos de idade:'.format(nomemaisvelho,maioridadehomem))
print('Ao todo {} mulheres tem menos de 20 anos.'.format(totmulher20))