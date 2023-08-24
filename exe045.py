import random
from time import sleep
coisas = ('pedra', 'papel', 'tesoura')
print('''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?: '))
pc = random.randint(0, 2)
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN') 
sleep(0.5)
print('PO')
if pc == 0: # Pedra
    if jogador == 0:
        print('\033[32m=-\033[m' * 15 )
        print(f'Computador jogou {coisas[pc]}\nJogador jogou {coisas[jogador]}')
        print('empate')
        print('\033[32m=-\033[m' * 15 )
    elif jogador == 1:
        print('\033[32m=-\033[m' * 15 )
        print(f'Computador jogou {coisas[pc]}\nJogador jogou {coisas[jogador]}')
        print('jogador ganhou')
        print('\033[32m=-\033[m' * 15 )
    elif jogador == 2:
        print('\033[32m=-\033[m' * 15 )
        print(f'Computador jogou {coisas[pc]}\nJogador jogou {coisas[jogador]}')
        print('computador ganhou')
        print('\033[32m=-\033[m' * 15 )
    else:
        print('JOGADA INVALIDA')
elif pc == 1: # Papel
    if jogador == 0:
        print('\033[32m=-\033[m' * 15 )
        print(f'Computador jogou {coisas[pc]}\nJogador jogou {coisas[jogador]}')
        print('Compotador ganhou')
        print('\033[32m=-\033[m' * 15 )
    elif jogador == 1:
        print('\033[32m=-\033[m' * 15 )
        print(f'Computador jogou {coisas[pc]}\nJogador jogou {coisas[jogador]}')
        print('Empate')
        print('\033[32m=-\033[m' * 15 )
    elif jogador == 2:
        print('\033[32m=-\033[m' * 15 )
        print(f'Computador jogou {coisas[pc]}\nJogador jogou {coisas[jogador]}')
        print('Jogador ganhou')
        print('\033[32m=-\033[m' * 15 )
    else:
        print('JOGADA INVALIDA')
elif pc == 2: # Tesoura
    if jogador == 0: 
        print('\033[32m=-\033[m' * 15 )
        print(f'Computador jogou {coisas[pc]}\nJogador jogou {coisas[jogador]}')
        print('Jogador ganhou')
        print('\033[32m=-\033[m' * 15 )
    elif jogador == 1:
        print('\033[32m=-\033[m' * 15 )
        print(f'Computador jogou {coisas[pc]}\nJogador jogou {coisas[jogador]}')
        print('Computador ganhou')
        print('\033[32m=-\033[m' * 15 )
    elif jogador == 2:
        print('\033[32m=-\033[m' * 15 )
        print(f'Computador jogou {coisas[pc]}\nJogador jogou {coisas[jogador]}')
        print('empate')
        print('\033[32m=-\033[m' * 15 )
    else:
        print('JOGADA INVALIDA') 
else:
        print('JOGADA INVALIDA')    