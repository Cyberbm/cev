import time
from random import randint

print('Olá, vou pensar em um número e quero que você adivinhe.')
tentativas = 0
time.sleep(2)
n1 = randint(0, 10)
while True:
    n = int(input('Que número eu pensei ?: '))
    tentativas += 1
    if n > n1:
        print('Menos.. Tente mais uma vez.')
    elif n < n1:
        print('Mais.. Tente mais uma vez.')
    elif n == n1:
        print('Você acertou! Parabéns!')
        break
    else:
        print('Informe um comando válido.')
print(f'Você precisou de {tentativas} tentativas para vencer.')