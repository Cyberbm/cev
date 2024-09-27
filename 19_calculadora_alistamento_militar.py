#=====================================================================
from datetime import date
#=====================================================================
#entrada de dados
ano_atual = date.today().year
ano = int(input('Digite o ano em que você nasceu: '))
calc = ano_atual - ano
#=====================================================================
#processamento de dados

if calc <= 17:
    saldo = ano_atual - ano
    print(f'''Quem nasceu em {ano} tem {saldo} anos.
Ainda faltam {18 - saldo} anos para se alistar.
Seu alistamento será em {ano + 18}''')

elif calc == 18:
    saldo = ano_atual - ano
    print(f'''Quem nasceu em {ano} tem {saldo} anos.
Você deve se alistar imediantamente!''')

else:
    saldo = ano_atual - ano
    print(f'''Você já passou do tempo de se alistar.
Você deveria ter se alistado há {saldo - 18} anos
Seu período de alistamento foi em {ano + 18}''')