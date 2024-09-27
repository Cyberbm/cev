import time
def menu():
    while True:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))

        print('''Escolha entre:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa.''')
#=================================================================
        opcao = input('Qual sua opção ?: ')
        if opcao == '1':
            print(f'A soma entre {n1} e {n2} é {n1+n2}')
            print('=' * 25 )
#=================================================================
        elif opcao == '2':
            print(f'O resultado da multiplicação de {n1} e {n2} é {n1*n2}')
            print('=' * 25 )
#=================================================================
        elif opcao == '3':
            if n1 > n2:
                print(f'{n1} é maior que {n2}')
            else:
                print(f'{n2} é maior que {n1}')
                print('=' * 25 )
        elif opcao == '4':
            return menu()
#==================================================================
        elif opcao == '5':
            print('Saindo do programa...')
            time.sleep(2)
            break
        else:
            print('Digite um comando válido.')
            print('=' * 25 )
menu()