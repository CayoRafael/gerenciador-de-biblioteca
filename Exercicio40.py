print('======='*20)
print('====CALCULE A MÉDIA DE NOTAS DE UM ALUNO EM DUAS AVALIAÇÕES======')
print('======='*20)
N1 = float(input('Qual a nota da primeira avaliação: '))
N2 = float(input('Qual a nota da segunda avalição: '))
MD = (N1+N2)/2
if MD >= 7:
    print('PARABÉNS VOCÊ FOI APROVADO! SUA MÉDIA FINAL FOI {}'.format(MD))
elif MD < 5:
    print('VOCÊ FOI REPROVADO! SUA MÉDIA FINAL FOI {}'.format(MD))
else:
    print('VOCÊ ESTÁ EM RECUPERAÇÃO SUA MÉDIA FINAL FOI {}'.format(MD))
print('======='*20)

