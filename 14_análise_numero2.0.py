v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))

if v1 > v2 and v1 > v3:
    print(f'O maior número é {v1}')
    if v2 < v3:
        print(f'O menor número é {v2}')
    else:
        print(f'O maior número é {v3}')

elif v2 > v1 and v2 > v3:
    print(f'O maior número é {v2}')
    if v1 < v3:
        print(f'O maior número é {v1}')
    else:
        print(f'O menor número é {v3}')
elif v3 > v1 and v3 > v2:
    print(f'O maior número é {v3}')
    if v1 < v2:
        print(f'O menor número é {v1}')
    else:
        print(f'O menor número é {v3}')