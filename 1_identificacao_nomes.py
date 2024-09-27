# programa para identificar alguns nomes. (prática)

nome = input('Qual seu nome?: ').title().strip()

if nome == 'Erick':
    print('Que nome bonito!')
    sobrenome = input('Qual seu sobrenome?: ').title().strip()
    if sobrenome == 'Martins':
        print(f'o sobrenome {sobrenome} é um sobrenome português!')
    else:
        print(f'{sobrenome} é um lindo sobrenome.')

elif nome in ['Pedro', 'Raphael', 'Rafael', 'Maria']:
    print('Seu sobrenome é popular no Brasil.')

elif nome in ['Ana', 'Cláudia', 'Jéssica', 'Juliana']:
    print(f'O nome {nome} é um nome feminino bonito.')

else:
    print(f'Tenha um bom dia {nome}!')