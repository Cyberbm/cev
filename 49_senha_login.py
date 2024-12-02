import re
from time import sleep

usuarios = []

#======================================================================================

def pagina_cadastro():

    while True:

        
        validar_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        cadastro_email = input('Crie seu email: ')
        if re.match(validar_email, cadastro_email):
            print('Email registrado')
            break
            
        else:
            print('Por favor, digite um email válido.')
            


#======================================================================================

    while True: 

        
        validar_senha = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        cadastro_senha = input('Crie sua senha: ')
        cadastro_senha_2 = input('Confirme sua senha: ')
        
        if cadastro_senha != cadastro_senha_2:
            print('As senhas não são compatíveis.')

        if re.match(validar_senha, cadastro_senha) and cadastro_senha == cadastro_senha_2:
            print('Senha registrada.')
            break
        
        else:
            print('A senha deve conter pelo menos 8 caracteres, sendo, um caractere maiúsculo, um minúsculo e um caractere especial.')
            
#======================================================================================

    while True:

        

            validar_nome_usuario = r'^[a-zA-Z0-9]+$'
            cadastro_usuario = input('Crie seu nome de usuário: ').capitalize().strip()
            if re.match(validar_nome_usuario, cadastro_usuario):
                print('Nome de usuário registrado.')
                break


            else:
                print('Crie um usuário com apenas letras e números.')

#======================================================================================

    usuario = {

        'email': cadastro_email,
        'usuario': cadastro_usuario,
        'senha': cadastro_senha

    }

    usuarios.append(usuario)
    print('Cadastro concluído.')
    return usuarios

#======================================================================================

def pagina_login():

    while True: 

        email_login = input('Digite seu email de login: ').strip()
        senha_login = input('Digite sua senha de login: ')
        for usuario in usuarios:
            if usuario['email'] == email_login and usuario['senha'] == senha_login:
                print(f'Seja bem vindo/a {usuario['usuario']}!')
                break

#======================================================================================    

def pagina_inicial():

    while True:

        opcao_1 = input(f'''{' ' * 10}Escolha uma das opções{' ' * 10}

[ 1 ] Cadastro
[ 2 ] Login
[ 3 ] Sair
            
''').strip()
        
        if opcao_1 == '1':
            pagina_cadastro()

        elif opcao_1 == '2':
            pagina_login()
        
        elif opcao_1 == '3':
            print('Encerrando...')
            sleep(2)
            break
        
        else:
            print('Por favor, escolha um comando válido.')


pagina_inicial()