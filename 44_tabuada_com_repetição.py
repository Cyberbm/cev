from time import sleep

while True:
    print('==' * 15)
    try:
        multi = int(input('Quer ver a tabuada de qual valor? [Números negativos para terminar]: '))
        if multi < 0:
            print('Finalizando...')
            sleep(2)
            break
        for n in range(1, 11):
            print(f'{multi} x {n} = {multi * n}')
    except ValueError:
        print('Por favor, digite um número.')