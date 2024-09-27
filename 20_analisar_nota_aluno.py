#=====================================================================
#entrada de dados.
nome = input('Informe o nome do aluno: ').strip().title()
nota_1 = float(input('Informe a nota da primeira prova do aluno: '))
nota_2 = float(input('Informe a nota da segunda prova do aluno: '))
#======================================================================
#lista de cores.
cores = {
    'Azul':'\033[94m',
    'Vermelho':'\033[91m',
    'Amarelo':'\033[93m',
    'RESET':'\033[0m'
}
#=====================================================================
#processamento de dados.

nota_total = (nota_1 + nota_2) / 2

if nota_total >= 7:
    print(f'O aluno {nome} foi {cores['Azul']}APROVADO!{cores['RESET']} com a média {cores['Azul']}{nota_total}{cores['RESET']}')

elif nota_total >= 5:
    print(f'O aluno {nome} com a média de {cores['Amarelo']}{nota_total}{cores['RESET']} está de {cores['Amarelo']}recuperação.{cores['RESET']}')

else:
    print(f'Infelizmente, o aluno {nome} foi {cores['Vermelho']}reprovado.')