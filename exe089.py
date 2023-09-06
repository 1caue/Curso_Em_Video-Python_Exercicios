list = []
cont = 0
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2
    list.append([nome, [n1, n2], m])
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if r == 'N':
        break
print('-=' * 18)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8} ')
print('-' * 36)
for i, a in enumerate(list):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 36)
    x = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if x == 999:
        print('FINALIZANDO....')
        break
    if x <= len(list) - 1:
        print(f'Notas de {list[x][0]} são {list[x][1]}')    
    print('<<< Volte sempre >>>')
