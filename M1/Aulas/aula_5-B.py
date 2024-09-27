#entrada de dados
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

#processamento de dados
n3 = (n1 + n2) / 2

#condição ternária
print('Você passou!' if n3 >=7 else 'Você repetiu de ano.')