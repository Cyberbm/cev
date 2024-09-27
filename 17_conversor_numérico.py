#=====================================================================
from textwrap import dedent
#=====================================================================
print(dedent(
    '''
    Bem vindo ao conversor númerico.
    Para converter para binário, digite [1]
    Para converter para octal, digite [2]
    Para converter para hexadecimal, digite [3]
    '''))
#=====================================================================
#lista de cores
cores = {
    'Roxo':'\033[1;95m',
    'Vermelho':'\033[1;91m',
    'Azul':'\033[1;94m',
    'Amarelo':'\033[1;93m',
    'Reset':'\033[0m'
}
#=====================================================================
#entrada de dados
numero = int(input('Digite um número para conversão: '))
escolha = int(input(dedent(
    '''
    Agora escolha entre:
    [ 1 ] Converter para BINÁRIO
    [ 2 ] converter para OCTAL
    [ 3 ] Converter para Hexadecimal
    ''')))
#=====================================================================
#processamento de dados

if escolha == 1:
    print(f'A conversão de {cores['Amarelo']}{numero}{cores['Reset']} para {cores['Azul']}BINÁRIO{cores['Reset']} é {cores['Azul']}{bin(numero)[2:]}{cores['Reset']}.')

elif escolha == 2:
    print(f'A conversão de {cores['Amarelo']}{numero}{cores['Reset']} para {cores['Roxo']}OCTAL{cores['Reset']} é {cores['Roxo']}{oct(numero)[2:]}{cores['Reset']}')

elif escolha == 3:
    print(f'A conversão de {cores['Vermelho']}{numero}{cores['Reset']} para {cores['Vermelho']}HEXADECIMAL{cores['Reset']} é {cores['Vermelho']}{hex(numero)[2:]}{cores['Reset']}')