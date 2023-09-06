from time import sleep
l = {}
p = []
l['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {l["nome"]} jogou?: ')) 
for c in range(0, tot):
    p.append(int(input(f'  Quantos gols na partida {c}?: ')))
l['gols'] = p[:]
l['total'] = sum(p)
sleep(1)
print('-=' * 30)
sleep(1)
print(l)
print('-=' * 30)
for k, v in l.items():
    sleep(1)
    print(f'o campo {k} tem o valor {v}')
print('-=' * 30)
sleep(1)
print(f'O jogador {l["nome"]} jogou {len(l["gols"])} partidas')
for i, a in enumerate(l['gols']):
    sleep(1)
    print(f'-> Na partida {i}, ele fez {a} gols')
print(f'Foi um total de {l["total"]} gols')
