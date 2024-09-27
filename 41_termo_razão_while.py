print('=-' * 16)
pt = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('=-' * 16)
#===================================================================
termo = pt
c = 1
#===================================================================
while c <= 10:
    print(f'{termo}',' ➜ ', end='')
    termo += razao
    c += 1
print('''Fim
''','=-' * 30)