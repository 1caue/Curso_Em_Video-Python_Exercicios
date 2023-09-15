# Declarção de Def ⇂
def jogador(nj='<desconhecido>', b=0):
    print(f'O jogador {nj} fez {b} gol(s) no campeonato.')

# Programa Principal ⇂
print('-' * 30)
nj = str(input('Nome do jogador: ')).strip()
g =  str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nj.strip() == '':
    jogador(b=g)
else:
    jogador(nj, g)
