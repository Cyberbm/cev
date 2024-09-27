from datetime import date #import para pegar a data atual do pc
ano = int(input('Que ano quer analisar ? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year #código para usar a data atual do pc

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')

else:
    print(f'O ano {ano} NÃO é BISSEXTO.')