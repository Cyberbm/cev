cores = {
    'Azul': '\033[94m',
    'Reset': '\033[0m'
}
soma = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma = soma + n
print(f'A soma de todos os números é {cores['Azul']}{soma}{cores['Reset']}')