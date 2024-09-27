#==============================================================
#entrada de dados
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
#===============================================================
#processamento de dados
if num1 > num2:
    print('O primeiro número é o maior número.')
elif num2 > num1:
    print('O segundo número é o maior número.')
else:
    print('Os dois números são iguais.')