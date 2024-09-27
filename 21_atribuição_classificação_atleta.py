from datetime import date
#===================================================================
#entrada de dados
print('Informe o gênero entre; Masculino ou Feminino.')
genero = input('Informe o gênero do(a) atleta: ').strip().title()
#===================================================================
#processamento de dados

if genero in ['Masculino', 'Feminino']:
    atribu = 'a' if genero == 'Feminino' else 'o'
    nome = input(f'Informe o nome d{atribu} atleta: ').strip().title()
    nascimento = int(input(f'Informe o ano de nascimento d{atribu} atleta: '))
    idade = date.today().year - nascimento
    
    if idade >= 26:
        print(f'{atribu.capitalize()} atleta {nome} tem a classificação: Master.')
    
    elif idade >= 20:
        print(f'{atribu.capitalize()} atleta {nome} tem a classificação: Sênior.')
    
    elif idade >= 15:
        print(f'{atribu.capitalize()} atleta {nome} tem a classificação: Júnior.')
    
    elif idade >= 10:
        print(f'{atribu.capitalize()} atleta {nome} tem a classificação: Infantil.')
    
    else:
        print(f'{atribu.capitalize()} atleta {nome} tem a classificação: Mirim.')

else:
    print('Informe o gênero entre Masculino ou Feminino.')