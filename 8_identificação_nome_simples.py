nome = str(input('Digite seu nome completo: ')).title().strip()
nome2 = nome.split()
print(f'''
Muito prazer em te conhecer!
Seu primeiro nome é {nome2[0]}
Seu último nome é {nome2[-1]}''')