from time import sleep
import re
#=============================================
cores = {
    'Preto':'\033[1;90m',
    'Branco':'\033[1;97m',
    'Vermelho':'\033[1;91m',
    'Reset':'\033[0m'
}
#===========================================

def nova_tarefa():
    
    alta, media, baixa = 0, 0, 0

    while True: 

            titulo = input('Título da tarefa: ').strip().title()

            descricao = input('Descrição da tarefa: ')

            vencimento = input('Digite a data de vencimento da sua tarefa (DDMMAAAA): ').strip()

            if not re.match(r'^\d{8}$', vencimento):
                print(f'{cores['Vermelho']}Por favor, digite uma data válida no formato DDMMAAAA.{cores['Reset']} ')
                continue
            else:
                data_valida = f'{vencimento[:2]}/{vencimento[2:4]}/{vencimento[4:]}'

            prioridade = input('Defina a prioridade ( Alta / Média / Baixa ): ').strip().upper()[0]
            if prioridade == 'A':
                prioridade = 'Alta'
                alta += 1
            elif prioridade == 'M':
                prioridade = 'Média'
                media += 1
            elif prioridade == 'B':
                prioridade = 'Baixa'
                baixa += 1
            else:
                print('Por favor, digite um comando válido.')
                continue
            
            tarefa = {
                'Título':titulo, 
                'Descrição':descricao,
                'Vencimento':data_valida, 
                'Prioridade':prioridade,
                'Concluída': False
            }
            return tarefa


tarefas = []

#============================================================

print(f'{cores['Branco']}{'=-=' * 5} Gerenciador de tarefas {'=-=' * 5}')

while True:
    print(f'''
Escolha entre as opções: 

[ 1 ]. Adicionar nova tarefa
[ 2 ]. Ver todas as tarefas
[ 3 ]. Marcar tarefa como concluída
[ 4 ]. Deletar tarefa
[ 5 ]. Sair

{cores['Reset']}''')

#===========================================================
    
    opcao = input('Escolha uma das opções: ').strip()

    if opcao == '1':
        nova = nova_tarefa()
        if nova:
            tarefas.append(nova)

#============================================================

    elif opcao == '2':
        if not tarefas:
            print('Ainda não há tarefas cadastradas.')
        else:
            for idx, tarefa in enumerate(tarefas, start=1):
                status = 'Concluída' if tarefa['Concluída'] else 'Pendente'
                print(f'''{'=-=' *5}
Tarefa {idx}:
Título: {tarefa['Título']}
Descrição: {tarefa['Descrição']}
Data de vencimento: {tarefa['Vencimento']}
Prioridade: {tarefa['Prioridade']}''')
    
#=============================================================================================

    elif opcao == '3':
        if not tarefas:
            print('Ainda não há tarefas cadastradas.')
        else:
            for idx, tarefa in enumerate(tarefas, start=1):
                status = 'Concluída' if tarefa['Concluída'] else 'Pendente'
                print(f'{idx}. {tarefa["Título"]} - Status: {status}')
            try:
                num_tarefa = int(input('Digite o número da tarefa que deseja marcar como concluída: ').strip())
                if 1 <= num_tarefa <= len(tarefas):
                    tarefas[num_tarefa - 1]['Concluída'] = True
                    print('Tarefa concluída.')
                else:
                    print('Número de tarefas inválido.')
            except ValueError:
                print('Por favor, digite um número válido.')

#=============================================================================================

    elif opcao == '4': 
        
        if not tarefas:
            print('Ainda não há tarefas cadastradas.')
        else:
            for idx, tarefa in enumerate(tarefas, start=1):
                print(f'{idx}. {tarefa["Título"]}')
            try:
                num_tarefa = int(input('Digite o número da tarefa que deseja deletar: '))
                if 1 <= num_tarefa <= len(tarefas):
                    tarefa_removida = tarefas.pop(num_tarefa - 1)
                    print(f'Tarefa "{tarefa_removida["Título"]}" excluída.')
                else:
                    print('Número de tarefa inválido.')
            except ValueError:
                print('Por favor, digite um número válido.')

#=================================================================================================

    elif opcao == '5':
        print('Finalizando...')
        sleep(2)
        break

    else:
        print('Por favor, escolha uma opção válida.')

    