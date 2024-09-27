from textwrap import dedent

nome = 'Ferreira'
cores = {
         'Roxo': '\033[95m',
         'Roxonegrito': '\033[1;95m',
         'Azul': '\033[94m',
         'Vermelhonegrito': '\033[1;91m',
         'VermelhosublinhadoFundoBranco': '\033[4;91;107m'
}

print(dedent(f'''
Usando listas para definir texto!
{cores['Roxo']}{nome}
{cores['Roxonegrito']}{nome}
{cores['Azul']}{nome}
{cores['Vermelhonegrito']}{nome}
{cores['VermelhosublinhadoFundoBranco']}{nome}{'\033[m'}
'''))