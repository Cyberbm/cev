import random
import textwrap
import time
from colorama import Fore, Back, Style, init
print(Fore.LIGHTYELLOW_EX + '-=-' * 24) #estilização.
print(Fore.RESET + '''        Vou pensar em um número entre 0 a 5. Tente adivinhar...   ''')
print(Fore.LIGHTYELLOW_EX + '-=-' * 24) #estilização.
n = int(input(Fore.RESET + 'Em que número estou pensando ?: ')) #entrada do usuário com formatação usando reset.
n1 = random.randint(0, 5) #processamento do computador.
print(Fore.LIGHTCYAN_EX + 'PROCESSANDO...')
time.sleep(2)
if n == n1:
    print(Fore.LIGHTYELLOW_EX + '-=-' * 24)
    print(Fore.LIGHTGREEN_EX + '''                        Parabéns! você acertou!''')
    print(Fore.LIGHTYELLOW_EX + '-=-' * 24)
    print(textwrap.dedent((
            Fore.LIGHTGREEN_EX + f'''
    O número escolhido foi {n}.
    O número que pensei foi {n1}
    ''')))
else:
    print(textwrap.dedent((Fore.RED +
                           f'''
    ERROU!!! o número escolhido por você foi {n}.
    O número que pensei foi {n1}.
    ''')))

#print(f'Parabéns, você acertou! o número é {n1}' if n == n1 else f'Você não acertou, o número é {n1}') # exemplo ternário :D