from time import sleep
#===================================================================

print('=-' * 16)
pt = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('=-' * 16)

#===================================================================

termo = pt
c = 1
total = 10

#===================================================================

while True:
    while c <= total:
        print(f'{termo}', ' ➜ ', end='')
        termo += razao
        c += 1
    print('Pausa')
    print('=-' * 30)
    termos_adic = int(input('Quantos termos você quer mostrar a mais? (Digite 0 para sair): '))
    if termos_adic == 0:
        break
    total += termos_adic

#===================================================================

print('Finalizando...')
sleep(2)
print('Progressão finalizada.')