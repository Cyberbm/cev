print(f'''{'=='*15}
{' '* 5} CAIXA ELETRÔNICO
{'=='*15}''')

try:
    valor = int(input('Qual valor você deseja sacar? R$: '))

except ValueError:
    print('Por favor, digite um número válido.')

total = valor
cedula = 50
total_cedula = 0

while True:
    
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    
    else:
        if total_cedula > 0:
            print(f'Você sacou {total_cedula} cédulas de {cedula}')
        
        if cedula == 50:
            cedula = 20
        
        elif cedula == 20:
            cedula = 10
        
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break