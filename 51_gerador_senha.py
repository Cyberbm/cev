import random
import string
import os
from time import sleep
from datetime import datetime

#=======================

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

#==================================================================

def salvar_senha(nome, senha):
    
    caminho_desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    pasta_senhas = os.path.join(caminho_desktop, 'Senhas')
    if not os.path.exists(pasta_senhas):
        os.makedirs(pasta_senhas)

    caminho_arquivo = os.path.join(pasta_senhas, 'senhas.txt')

    data_atual = datetime.now().strftime('%d/%m/%Y')
    linhas_existentes = []

    # Lê o conteúdo do arquivo, caso já exista
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r') as arquivo:
            linhas_existentes = arquivo.readlines()

    # Atualiza ou adiciona a nova senha
    with open(caminho_arquivo, 'w') as arquivo:
        senha_atualizada = False
        for linha in linhas_existentes:
            if linha.startswith(f'{nome}:'):
                arquivo.write(f'{nome}: {senha} criado: {linha.split("criado:")[1].split()[0]} ultima vez editado: {data_atual}\n')
                senha_atualizada = True
            else:
                arquivo.write(linha)

        # Adiciona a senha caso seja nova
        if not senha_atualizada:
            arquivo.write(f'{nome}: {senha} criado: {data_atual} ultima vez editado: {data_atual}\n')

#==================================================================

try:
    tamanho_desejado = int(input('Digite o tamanho desejado para a senha: '))

except ValueError:
    print('Por favor, digite um número válido.')

nome_aplicativo = input('Qual é o nome atrelado à senha? (app, email, etc...): ').strip().title()

senha = gerar_senha(tamanho_desejado)
print('Senha gerada:', senha)

salvar_senha(nome_aplicativo, senha)

#==================================================================
while True:
    opcao = input('Gostaria de gerar mais senhas? (S/N): ').strip().upper()[0]

    if opcao == 'S':
        nome_aplicativo = input('Qual é o nome atrelado à senha? (app, email, etc...): ').strip().title()
        tamanho_desejado = int(input('Digite o tamanho desejado para a senha: '))
        senha = gerar_senha(tamanho_desejado)
        print('Senha gerada:', senha)
        salvar_senha(nome_aplicativo, senha)
    
    elif opcao == 'N':
        print('Finalizando...')
        sleep(2)
        break
    
    else:
        print("Opção inválida. Por favor, escolha 'S' para sim ou 'N' para não.")
