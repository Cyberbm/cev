'''from math import factorial
n = int(input('Digite o número para calcular o fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')'''

n = int(input('Digite o número para calcular o fatorial: '))
c = n
f = 1
while c > 0:
    print(f'{c}','x ' if c > 1 else '= ',end='')
    f = f * c
    c -= 1
print(f'''{f}
O fatorial de {n} é {f}''')