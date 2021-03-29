import random
num=random.randint(1,2)
jogo=int(input('qual e o numero que eu pencei?'))
acertou = jogo == num
vezes=4
for c in range(1,vezes):
    faca=int(input('voce errou tenta novamente'))
    ja=acertou
    if ja:
        print('boa voce acertou')
    else:
        print('voce errou mano')
