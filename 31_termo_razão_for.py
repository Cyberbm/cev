cores = {

    'Negrito': '\033[1m',
    'Reset': '\033[0m'
}

print(cores['Negrito'], '-=' * 20, cores['Reset'])
print(f'''{' ' * 10}{cores['Negrito']}10 TERMOS DE UMA PA''')
print(cores['Negrito'], '-=' * 20, cores['Reset'])

primeiro_termo = int(input(f'{' '*3}Primeiro termo: '))

razao = int(input(f'{' '*3}Razão: '))

decimo = primeiro_termo + (10-1) * razao

for c in range(primeiro_termo, decimo + razao, razao):
    print(c, end=' -> ')

print('Fim!')

print(cores['Negrito'], '-=' * 30)