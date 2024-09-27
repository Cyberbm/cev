import textwrap
distancia = float(input('Qual a distância da sua viagem ?: '))
calculo1 = (distancia * 0.45) #para viagens mais longas
calculo2 = (distancia * 0.50) #para viagens menores

if distancia >= 201:
    print(textwrap.dedent(
        f'''
        Você está prestes a começar uma viagem de {distancia}km
        O preço da sua passagem será R${calculo1 :.2f}'''))


elif distancia <= 200:
    print(textwrap.dedent(
        f'''
        Você está prestes a começar uma viagem de {distancia}km
        O preço da sua passagem será R${calculo2:.2f}'''))