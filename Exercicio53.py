#crie um programa que leia uma frase qualquer e diga se ela é um polidromo, desconsiderando os espaços.
#ex: apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo,anotaram a data da maratona.
frase = str(input('Escreva uma frase: ')).strip().upper() #strip tira os espaços antes e depois upper deixa maiuscula
palavras = frase.split()   #separa a frase em palavras
junto = ''.join(palavras)  #junta tudo tirando os espaços das frases
inverso = junto [::-1] #resolução com fatiamento.
#esta outra é a resolução com o for: ai é só apagar a linha acima.
#inverso = ''
#for letra in range(len(junto) - 1, -1,-1): #len(junto) foi da  a ultima letra até a primeira é o segundo -1, o outro é -1 passo.
      #inverso += junto[letra]
print(' O inverso de {} é {} '. format(junto,inverso))
if inverso == junto:
    print('Temos um Palindromo!')
else:
    print('A frase digitada não é Palindromo!')