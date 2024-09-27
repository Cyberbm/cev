print('Bem vindo!')
#==================================================================
#entrada de dados
primeiro_segmento: float = float(input('Informe o primeiro segmento do triângulo: '))
segundo_segmento = float(input('Informe o segundo segmento do triângulo: '))
terceiro_segmento = float(input('Informe o terceiro segmento do triângulo: '))
if primeiro_segmento < segundo_segmento + terceiro_segmento and segundo_segmento < primeiro_segmento + terceiro_segmento and terceiro_segmento < primeiro_segmento + segundo_segmento:

  if primeiro_segmento + segundo_segmento > terceiro_segmento or primeiro_segmento + terceiro_segmento > segundo_segmento:
    print('Você pode formar um triângulo')
    
    if primeiro_segmento == segundo_segmento and primeiro_segmento == terceiro_segmento:
        print('Seu triângulo é equilátero. Todas as formas são iguais.')

    elif primeiro_segmento == segundo_segmento and primeiro_segmento != terceiro_segmento:
        print('Seu triângulo é isósceles. Dois lados são iguais.')

    elif primeiro_segmento != segundo_segmento and segundo_segmento != terceiro_segmento and primeiro_segmento != terceiro_segmento:
        print('Seu triângulo é escaleno. Todos os lados são diferentes.')

else:
    print('Você não pode formar um triângulo.')