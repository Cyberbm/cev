while True:
    genero = input('Por favor, informe seu gênero entre [ M / F ]: ').upper().strip()[0]
    if genero == 'M':
        print('Gênero masculino registrado com sucesso.')
        break
    elif genero == 'F':
        print('Gênero feminino registrado com sucesso.')
        break
    else:
        print('Por favor, informe um dos dois gêneros.')