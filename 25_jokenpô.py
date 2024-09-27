from time import sleep
from random import choice
#===================================================================
#lista de cores
cores = {
    'Azul': '\033[1;94m',
    'Vermelho': '\033[1;91m',
    'Roxo': '\033[1;95m',
    'Amarelo': '\033[1;93m',
    'Ciano': '\033[1;96m',
    'Reset': '\033[0m'
}
#===================================================================
#entrada de dados
print(cores['Ciano'],'-=' * 20, cores['Reset'])
escolha = input(f'''{cores['Roxo']}Escolha entre uma das opções:
[ 1 ] Pedra.
[ 2 ] Papel.
[ 3 ] Tesoura.
Qual sua escolha ?: {cores['Reset']}''')
print(cores['Ciano'], '-='*20, cores['Reset'])
print(cores['Roxo'],' ' * 16,'JO',' ' * 10)
sleep(1)
print(' ' * 17, 'KEN', ' ' *10)
sleep(1)
print(' ' * 17, 'PO!', ' ' * 10,cores['Reset'])
print(cores['Ciano'], '-=' * 20, cores['Reset'])
#===================================================================
#lista de escolha
resposta = ['Pedra', 'Papel', 'Tesoura']
#===================================================================
#processamento de dados
jogada_pc = choice(resposta)

if (escolha == '1' and jogada_pc == 'Pedra') or (escolha == '2' and jogada_pc == 'Papel') or (escolha == '3' and jogada_pc == 'Tesoura'):
    cor, mensagem = cores['Amarelo'],'Você empatou!'

elif (escolha == '1' and jogada_pc == 'Tesoura') or (escolha == '2' and jogada_pc == 'Papel') or (escolha == '3' and jogada_pc == 'Pedra'):
    cor, mensagem = cores['Azul'], 'Você ganhou! parabéns!'

elif (escolha == '1' and jogada_pc == 'Papel') or (escolha == '2' and jogada_pc == 'Tesoura') or (escolha == '3' and jogada_pc == 'Pedra'):
     cor, mensagem = cores['Vermelho'], 'Você perdeu.'
else:
    print('Digite um comando válido.')

print(f'{cores['Roxo']}Sua jogada foi {resposta[int(escolha) - 1]} e a jogada do computador foi {jogada_pc}!{cores['Roxo']} {cor}{mensagem}{cores['Reset']}')