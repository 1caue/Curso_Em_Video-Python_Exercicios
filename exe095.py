from time import sleep
t = []
l = {}
p = []
while True:
    l['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {l["nome"]} jogou?: ')) 
    p.clear()
    for c in range(0, tot):
        p.append(int(input(f'  Quantos gols na partida {c}?: ')))
    l['gols'] = p[:]
    l['total'] = sum(p)
    t.append(l.copy())
    while True:
        r = str(input('Quer continuar?: ')).upper()[0]
        if r in 'SN':
            break
        else:
            r = str(input('ERRO!, Digite apenas S ou N!: ')).upper()[0]
    if r == 'N':
        break
print('-=' * 30)
print(' cod ', end='')
for i in l.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(t):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    b = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if b == 999:
        break
    if b >= len(t):
        print(f'ERRO! Não existe jogador com código {b}!')
    else:
        print(f'------ LEVANTAMENTO DO JOGADOR {t[b]["nome"]} ------')
        for i, gl in enumerate(t[b]["gols"]):
            sleep(1)
            print(f'    No jogo {i+1} fez {gl} gols.')
    print('-' * 30)
sleep(1)
print('<<<<< VOLTE SEMPRE >>>>>')    
