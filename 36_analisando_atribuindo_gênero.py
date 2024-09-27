pessoas = []
contador_m = 0
contador_f = 0
contador_nb = 0
acumulador = 0
atribu = []
#===================================================================
cores = {
    'Negrito':'\033[1m',
    'Azul':'\033[1;94m',
    'Roxo':'\033[1;95m',
    'Reset':'\033[0m'
}
#===================================================================
for i in range(1, 6):
    print(cores['Azul'],'==' * 5, f'{i}ª PESSOA','==' * 5, cores['Reset'])
    nome = input('Qual nome da pessoa ?: ').strip().title()
    idade = int(input('Qual a idade da pessoa ?: '))
    acumulador = acumulador + idade
    genero = input('Qual o gênero que a pessoa se identifica ?(M/F/NB): ').strip().upper()
    pessoa = {'nome': nome, 'idade': idade, 'genero': genero}

    pessoas.append(pessoa)

    if genero == 'M':
        contador_m += 1
    if genero == 'F':
        contador_f += 1
    if genero == 'NB':
        contador_nb += 1

atribu_m = 'ens' if contador_m > 1 else ''
atribu_f = 'es' if contador_f > 1 else ''
atribu_nb = 's' if contador_nb > 1 else ''


media = acumulador / 5
mais_velho = pessoas[0]
mais_novo = pessoas[0]

for pessoa in pessoas:
    if pessoa['idade'] > mais_velho['idade']:
        mais_velho = pessoa
    if pessoa['idade'] < mais_novo['idade']:
        mais_novo = pessoa

#===================================================================
for pessoa in pessoas:
    print(f'{pessoa['nome']} tem {pessoa['idade']} anos e se identifica como {pessoa['genero']}')

print(f'No total há {contador_f} mulher{atribu_f}, {contador_m} homem{atribu_m} e {contador_nb} não binário{atribu_nb}. \nE a média de idade é de {media :.0f} anos.')


print(f'''{cores['Azul']}{mais_velho['nome']} é a pessoa mais velha com {mais_velho['idade']} anos{cores['Reset']}.
{cores['Roxo']}{mais_novo['nome']} é a pessoa mais nova com {mais_novo['idade']} anos.''')