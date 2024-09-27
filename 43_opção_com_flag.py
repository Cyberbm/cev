tentativas = 0
soma = 0 
while True:
    try:
        n = int(input('Digite um valor [ 999 para parar]: '))
        if n == 999:
            break
        soma += n
        tentativas += 1 #fazendo assim para poder contar caso seja válido. Antes o que eu tinha feito, foi de por os controladores depois do ValueError, o que não estava contando, caso ouvesse um erro no meio da repetição.
    except ValueError:
        print('Por favor, digite um número.')
print(f'A soma dos {tentativas} valores foi {soma}')