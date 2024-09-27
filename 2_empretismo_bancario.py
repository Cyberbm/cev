cores = {
    'Azul': '\033[1;94m',
    'Vermelho': '\033[1;91m',
    'Verde': '\033[1;92m',
    'Roxo': '\033[1;95m',
    'Reset': '\033[0m'
}
#=================================================================
try:
    valor_imovel = float(input('Qual valor do imóvel que deseja comprar?: '))

    salario = float(input('Digite seu salário R$:'))

    financiamento_meses = int(input('Em quantos meses você deseja pagar o financiamento ? '))
except ValueError:
    print('Informe um número válido.')
#=================================================================
calculo_casa = valor_imovel * 0.58
calculo_financiamento = valor_imovel / financiamento_meses
calculo_salario = salario * 0.30
#=================================================================
#saída de dados. 

if calculo_financiamento >= calculo_salario:
    print(f'{cores['Vermelho']}Seu empretismo foi negado.{cores['Reset']}')
    print(f'O valor mensal da prestação do financiamento de {cores['Verde']} R$ {calculo_financiamento:.2f}{cores['Reset']} excede 30% do seu salário {cores['Verde']}R$ {calculo_salario:.2f}{cores['Reset']}')

else:
    print(f'Financiamento {cores['Azul']}aprovado! {cores['Reset']}')
    print(f'O valor da prestação mensal do financiamento será de {cores['Verde']} R$ {calculo_financiamento:.2f}{cores['Reset']}')
    print(f'{cores['Azul']}Pababéns pelo seu financiamento!{cores['Reset']}')
    print(f'Com juros, o valor total do imóvel fica em {cores['Verde']}R'
          f'${valor_imovel + calculo_casa:.2f}')
