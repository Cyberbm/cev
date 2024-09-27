nome = str(input('Digite seu nome completo: ')).strip()
nome1 = nome.replace(' ', '')
nome2 = nome.split()
print(f'''
Analisando seu nome...
Seu nome em minúsculo é {nome.lower()}
Seu nome em maiúsculo é {nome.upper()}
Seu nome tem ao todo {len(nome1)} letras
Seu primeiro nome é {nome2[0]} e ele tem {len(nome2[0])} letras.''')

frase = str(input('Digite uma frase: ')).lower().strip()
print(f'''
A letra "a" aparece {frase.count('a')} vezes.
A primeira letra "a" aparece na posição {frase.find('a') + 1}.
A última letra "a" aparece na posição {frase.rfind('a')+1}
''')