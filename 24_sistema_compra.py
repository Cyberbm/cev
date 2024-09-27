print('\033[1m', '='*10, 'LOJA', '='*10, '\033[0m')
preco = int(input('Digite o preço das compras: '))
print('\033[1mFORMA DE PAGAMENTO\033[0m')
print('''[ 1 ] À vista dinheiro/pix
[ 2 ] À vista cartão de crédito/débito
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

escolha = input('Escolha a forma de pagamento (de 1 a 4): ')

if escolha == '1':
    print(f'''Sua compra de R${preco:.2f} recebe um desconto de R${preco * 0.10:.2f} à vista!
E custará R${preco - preco * 0.10:.2f}''')

elif escolha == '2':
    print(f'''Sua compra de R${preco :.2f} recebe um desconto de R${preco * 0.05:.2f} à vista no cartão!
E custará R${preco - preco * 0.05:.2f}''')

elif escolha == '3':
    print(f'''Você está comprando em 2x sem juros no cartão.
Total de 2 parcelas de R${preco * 0.50:.2f}''')

elif escolha == '4':
    parcelas = int(input('Em quantas parcelas deseja comprar ?: '))
    print(f'''Sua compra será parcelada em {parcelas}x de R${preco / parcelas * 1.20 :.2f}
Sua compra de R${preco:.2f} custará {(preco) * 1.20 :.2f} com juros.''')

else:
    print('Digite um comando válido.')