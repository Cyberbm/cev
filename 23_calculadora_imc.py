#biblioteca
from time import sleep
#===================================================================
#mensagem de boas vinda ao aplicativo
print('Olá, bem vindo a calculadora de imc.')
#===================================================================
#entrada de dados
nome = input('Qual seu nome ?: ').strip().title()
genero = input('Qual seu gênero ? (escolha entre masculino ou feminino): ').strip().title()
#====================================================================
#processamento :D

if genero in ['Masculino', 'Feminino']:
    atribuicao = 'a' if genero == 'Feminino' else 'o'
    print(f'Seja muito bem vind{atribuicao} {nome}!')
    peso = float(input('Quanto você pesa ? (Kgs): '))
    altura = float(input('Qual sua altura ? (M): '))
    imc = peso / (altura ** 2)
    classificacao = {'abaixo do peso normal': 18.5,
                     'peso normal': 24.9,
                     'sobrepeso': 29.9,
                     'obesidade grau 1': 34.9,
                     'obesidade grau 2': 39.9,
                     'obesidade grau 3': 40.0
                     }

    print(f'Aguarde enquanto calculamos seu imc {nome}')

    sleep(2)

    if imc < classificacao['abaixo do peso normal']:
        status = 'abaixo do peso'
    
    elif imc <= classificacao['peso normal']:
        status = 'peso normal'
    
    elif imc <= classificacao['sobrepeso']:
        status = 'sobrepeso'
    
    elif imc <= classificacao['obesidade grau 1']:
        status = 'obesidade grau 1'
    
    elif imc <= classificacao['obesidade grau 2']:
        status = 'obesidade grau 2'
    
    else:
        status = 'obesidade grau 3'
    print(f'{nome} seu imc é de {imc:.2f} considerado {status}.')