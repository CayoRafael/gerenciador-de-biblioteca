while True:
    print('\033[1;33m======='*20)
    print('\033[1;97m===== \033[1;34m CALCULE A MÉDIA DE NOTAS DE UM ALUNO EM DUAS AVALIAÇÕES \033[1;32m \033[1;97m====== \033[1;32m')
    print('======='*20)
    AL = str(input('\033[1;97mNome do Aluno: ')).strip().upper()
    N1 = float(input('Nota da 1ª Avaliação: '))
    N2 = float(input('Nota da 2ª Avaliação: '))
    N3 = float(input('Nota da 3ª Avaliação: '))
    MD = (N1 + N2 + N3) / 3
    print(f'Notas obtidas pelo aluno {N1} + {N2} + {N3}.')
    print(f'SUA MÉDIA FINAL FOI {MD:.1f}.')
    if MD >= 7:
        print(f'PARABÉNS {AL}, VOCÊ FOI \033[1;32m APROVADO! \033[1;97m')
    elif MD < 7:
        print(f'VOCÊ FOI \033[1;31m REPROVADO \033[1;97m {AL}, ESTUDE MAIS!')
    print('=======' * 20)
    resp = input('Deseja continuar e inserir mais alunos e notas? [S/N]: ').strip().upper()
    print('=======' * 20)
    if resp == 'N':
        print('PROGRAMA ENCERRADO!')
        break

