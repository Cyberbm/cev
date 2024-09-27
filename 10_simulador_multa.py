import textwrap
from colorama import Fore
from time import sleep

velocidade = float(input('Qual a velocidade atual do carro?: '))

print('PROCESSANDO... AGUARDE...')

sleep(3)

multa = (velocidade - 80) * 7 

if velocidade >= 81: 
    print(Fore.LIGHTRED_EX + '-=-' * 24)
    print(textwrap.dedent((Fore.LIGHTRED_EX +
    f'''
    MULTADO!!!
    Você excedeu o limite permitido de 80km/h
    Você deve pagar uma multa de R${multa :.2f}
    ''')))
    print(Fore.LIGHTRED_EX + '-=-' * 24)
    print(Fore.LIGHTBLUE_EX + '''           Dirija com cuidado e respeite as leis de trânsito!
                         Tenha um bom dia.''')
    
else:
    print(Fore.LIGHTGREEN_EX + '-=-' * 24)
    print(Fore.LIGHTGREEN_EX + '''
                Tenha um bom dia! Dirija com segurança!
    ''') #mensagem final
    print(Fore.LIGHTGREEN_EX + '-=-' * 24)