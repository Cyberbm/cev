cor = {
    'Branco':'\033[1;97m',
    'Reset':'\033[0m'
}

maior_18, mulheres_20, homens = 0, 0, 0

while True:
    print(f'''{cor['Branco']}{'== * =='*5}
{' '*7}CADASTRO DE PESSOAS
{'== * =='*5}''')
    
    try:
        idade = int(input('Digite a idade da pessoa: '))
        if idade >= 18:
            maior_18 += 1
        genero = input('Escolha o gênero desta pessoa [ M / F ]: ').strip().upper()[0]
        if genero in 'M':
            homens += 1
        elif genero in 'F' and idade <= 20:
            mulheres_20 += 1
        opcao = input('Quer continuar? [ S / N ]: ').strip().upper()[0]
        if opcao in 'S':
            continue
        elif opcao in 'N':
            break
        else:
            print('Digite uma opção válida.')
    
    except ValueError:
        print('Por favor, digite um número.')

print(f'''{'Foi' if mulheres_20 == 1 else 'Foram'} cadastrada{'s' if mulheres_20 != 1 else ''} {mulheres_20} mulher{'es' if mulheres_20 != 1 else ''} abaixo de 20 anos.
{homens} homem{'s' if homens != 1 else ''} {'foi' if homens == 1 else 'foram'} cadastrado{'s' if homens != 1 else ''}.
E {maior_18} pessoa{'s' if maior_18 != 1 else ''} cadastrada{'s' if maior_18 != 1 else ''} são maiores de idade.''')

    
    