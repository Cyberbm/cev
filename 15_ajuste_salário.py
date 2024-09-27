salario = float(input('Qual é o salário do funcionário ?: '))

if salario >= 1250.00:
    print(f'O salário de R${salario:.2f} do funcionário, agora será de R${salario * 1.10 :.2f} com um aumento de 10%.')

else:
    print(f'O salário de R${salario:.2f} do funcionário, agora será de R${salario * 1.15 :.2f} com um aumento de 15%.')