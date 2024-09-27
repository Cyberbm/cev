from colorama import Fore

print(Fore.LIGHTMAGENTA_EX + '-=-' * 24)
print( '''                        Analisador de triângulo''')
print('-=-' * 24)
primeiro_s = float(input(Fore.RESET + 'Digite o primeiro seguimento do triângulo: '))
segundo_s = float(input('Digite o segundo seguimento do triângulo: '))
terceiro_s = float(input('Digite o terceiro segmento do triângulo: '))

if (primeiro_s + segundo_s > terceiro_s) and (primeiro_s + terceiro_s >segundo_s) and (segundo_s + terceiro_s > primeiro_s):
    print(f'Os segmentos acima {Fore.LIGHTBLUE_EX} PODEM {Fore.RESET} formar um triângulo!')

else:
    print(f'Os seguimentos acima {Fore.LIGHTRED_EX}NÃO {Fore.RESET}podem formatar um triângulo.')