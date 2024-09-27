
peso_maior = None
peso_menor = None

#peso_maior e peso_menor começam com None pq ainda não há pesos a serem comparados. Na primeira iteração, estes valores serão definidos como primeiro peso
#===================================================================
#processamento e analise dados.

for pessoa in range(1, 6):
    peso = float(input(f'Qual o peso da {pessoa}ª pessoa?: '))

#Aq o código está verificando cada iteração, vendo se o peso é maior ou menor, e atualiza essas variáveis conforme o necessário.
    if peso_maior is None and peso_menor is None:
        peso_maior = peso
        peso_menor = peso #

#A partir daq, verifica se são maiores ou menores a cada iteração.
    if peso > peso_maior:
        peso_maior = peso

    if peso < peso_menor:
        peso_menor = peso

#===================================================================
print(f'''O maior peso lido foi {peso_maior}Kgs
O menor peso registrado foi {peso_menor}Kgs''')