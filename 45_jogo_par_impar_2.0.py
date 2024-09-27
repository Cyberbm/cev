from random import randint
from time import sleep

cores = {
    'Branco':'\033[1m',
    'Azul':'\033[94m',
    'Vermelho':'\033[91m',
    'Reset':'\033[0m'
}
#==================================================================
while True:
    print(f'''{cores['Branco']}{'<=-=>'*6}
{' '*3}VAMOS JOGAR PAR OU ÍMPAR
{'<=-=>'*6}{cores['Reset']}''')
    n = randint(1, 10)
    try:
        valor = int(input('Digite um valor: '))
        if valor < 0:
            break
        escolha = input('Acha que o resultado será PAR ou ÍMPAR?: ').strip().upper()[0]
#========================= PAR =========================        
        if escolha == 'P':
            if (valor + n) % 2 == 0:
                print(f'''Você ganhou!
Você jogou {valor} e o computador jogou {n}. O total é {valor + n} que é um número PAR.''')
                continue           
            elif (valor + n) % 2 == 1:
                print(f'''Você perdeu...
Você jogou {valor} e o computador jogou {n}. O total é {valor + n} que é ÍMPAR''')
                break
#========================= ÍMPAR =========================
        elif escolha == 'I' or escolha == 'Í':
            if (valor + n) % 2 == 1:
                print(f'''Você ganhou!
Você jogou {valor} e o computador jogou {n}. O total é {valor + n} que é um número ÍMPAR.''')
                continue
            elif (valor + n) % 2 == 0:
                print(f'''Você perdeu...
Você jogou {valor} e o computador jogou {n}. O total é {valor + n} que é PAR''')
                break
#=================================================================     
        else:
            print('Escolha entre [ P / I ]')
    except ValueError:
        print('Por favor, digite um número.')