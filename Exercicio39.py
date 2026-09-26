from datetime import date
Atual = date.today().year
import emoji
from emoji import emojize
print('=============='*9)
print(emoji.emojize('\033[1;32m=====\033[1;34m  RECRUTAMENTO\033[1;32m  MILITAR \033[1;33m  DO \033[1;m  BRASIL :yellow_circle: :green_circle: :blue_circle: :flexed_biceps: \033[1;32m  ========'))
print('=============='*9)
Nascimento = int(input('Qual seu ano de nascimento: '))
Idade = Atual - Nascimento
if Atual - Nascimento == 18:
    print(emoji.emojize('\033[1;m Você tem {} anos, \033[1;32m  SEJA BEM VINDO AO EXÉRCITO BRASILEIRO! :writing_hand: '.format(Idade)))
elif Atual - Nascimento <= 17:
    print(emoji.emojize('Você ainda tem {} anos, NOS VEREMOS EM BREVE: :handshake:'.format(Idade)))
else:
    print(emoji.emojize('\033[1;m Você tem {} anos! Já deveria ter se alistado em {} ! :old_man: '.format(Idade,Atual-18)))
print('=============='*9)
print(emoji.emojize('\033[1;32m=== \033[1;33mEXÉRCITO\033[1;32m BRASILEIRO\033[1;34m BRAÇO\033[1;33m FORTE\033[1;32m E \033[1;34mMÃO\033[1;m AMIGA\033[1;32m :yellow_circle: :green_circle: :blue_circle: :flexed_biceps: ===='))
print('=============='*9)