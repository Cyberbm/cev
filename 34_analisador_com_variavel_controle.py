from datetime import date

ano_atual = date.today().year
#===================================================================
#variaveis de controle.
control1 = 0
control2 = 0
#===================================================================
#processamento de dados.
for c in range(1,8):
    nascimento = int(input(f'Em que ano a {c}ª pessoa nasceu ?'))

    idade = ano_atual - nascimento 

    if idade >= 18 :
        control1 += 1 
    
    else:
        control2 += 1 
#===================================================================
print(f'Ao todo, {control1} pessoas são maiores de idade e {control2} são menores de idade')