from colorama import Fore
numero = int(input(Fore.MAGENTA + 'Me diga um número qualquer: '))
if numero % 2 == 1:
    print(Fore.RESET + f'Este número é {Fore.LIGHTBLUE_EX}IMPAR')
else:
    print(Fore.RESET + f'O número {numero} é {Fore.LIGHTBLUE_EX}PAR')