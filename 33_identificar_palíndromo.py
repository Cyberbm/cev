cores = {
    'Azul': '\033[1;34m',
    'Vermelho': '\033[1;31m',
    'Reset': '\033[0m'
}

#===============================================================
palavra = input('Digite uma palavra ou frase: ').strip().lower()

palavra_sem_espaco = palavra.replace(' ', '')

palavra_invertida = ''
#=================================================================
for letra in palavra_sem_espaco:
    palavra_invertida = letra + palavra_invertida


if palavra_sem_espaco == palavra_invertida:
    print(f'{palavra} {cores['Azul']}é um palíndromo!{cores['Reset']}')

else:
    print(f'{palavra}{cores['Vermelho']} Não é um palíndromo.')