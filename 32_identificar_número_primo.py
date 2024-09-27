cores = {
    'Vermelho claro': '\033[31m',
    'Azul claro': '\033[34m',
    'Reset': '\033[0m'
}
#====================================
#processamento de dados do contador e divisor
divisivel = 0
#====================================
n = int(input('Digite um número para saber se ele é primo ou não: '))
for c in range(1, n+1):
    if n % c == 0:
        print(cores['Azul claro'], end=' ')
        divisivel += 1
    else:
        print(cores['Vermelho claro'], end=' ')
    print(f'{c}', end=' ')
print(f'''
{cores['Reset']}O número {n} é divisível apenas {divisivel} vezes.''')
if divisivel == 2:
    print(f'O número {n} é um número primo!.')
else:
    print(f'{n} não é um número primo')