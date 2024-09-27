import random

n = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

lista = [n, n2, n3, n4]

r = random.choice(lista)

print('O aluno escolhido foi:', r)