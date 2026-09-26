import random
print ('SORTEIO DE ALUNOS')
n1 = (input('Primeiro Aluno: '))
n2 = (input('Segundo Aluno '))
n3 = (input('Terceiro Aluno '))
n4 = (input('Quarto Aluno '))
lista = [n1,n2,n2,n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}',format(escolhido))