gasto, produtos_acima_1000 = 0, 0
nome_produto_mais_barato = None
produto_mais_barato = None

while True:
    n_produto = input('Qual o nome do produto?: ').strip()
    try:
        preço = int(input('Qual o preço do produto?: '))
        gasto += preço

        if produto_mais_barato is None or preço < produto_mais_barato:
            produto_mais_barato = preço
            nome_produto_mais_barato = n_produto

        if preço > 1000:
            produtos_acima_1000 += 1

        escolha = input('Quer continuar ? [ S / N ]: ').strip().upper()[0]

        if escolha == 'S':
            continue
        else:
            break

    except ValueError:
        print('Por favor, digite um valor válido.')

print(f'''O total da compra foi de R${gasto:.2f}
{produtos_acima_1000} {'Produto' if produtos_acima_1000 == 1 else 'Produtos'} acima de R$1000.00
O produto mais barato foi {nome_produto_mais_barato}, que custou R${produto_mais_barato}''')