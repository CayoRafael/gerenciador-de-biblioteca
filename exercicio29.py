import emoji
from emoji import emojize

V = float(input(emoji.emojize('Digite a velocidade do seu carro: :oncoming_automobile: ')))
if V > 80:
    multa = (V - 80) * 7
    print(emoji.emojize('MULTADO! Você excedeu o limite de velocidade em {} KM/h :face_screaming_in_fear: :police_car:'.format (V-80)))
    print(emoji.emojize('Por isso recebeu uma multa de {} reais e 7 pontos na carteira. :confounded_face:'.format(multa)))
else:
    print(emoji.emojize('Muito bem você é um condutor prudente! Parabéns: :clapping_hands: :trophy:'))
