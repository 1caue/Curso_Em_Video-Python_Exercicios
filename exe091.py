from random import randint
from time import sleep
from operator import itemgetter
jg = {'jogador 1': randint(1, 6), 
      'jogador 2': randint(1, 6), 
      'jogador 3': randint(1, 6),
      'jogador 4': randint(1, 6)}
ranking = []
print('Valores sorteados:')
print('-=' * 30)
for k, v in jg.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
print('-=' * 30)
print('   == RANKING DOS JOGADORES ==')
ranking = sorted(jg.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(1)
    print(f'     {i+1} lugar: {v[0]} com {v[1]}')
