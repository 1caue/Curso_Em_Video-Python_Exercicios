l = []
resp = ''
while True:
    n = int(input('Digite um valor: '))
    if n not in l:
        l.append(n)
        print('Valor adicionado com sucesso...')
    else: 
        print('Valor duplicado! Não vou adicionar')
    resp = str(input('Quer continuar? [S/N]').upper().strip())
    if resp in 'Nn':
        break
print('-=' * 30)
l.sort()
print(f'Você digitou os valores {l}')
