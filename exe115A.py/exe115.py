from fun import *
from time import sleep

while True:
    r = menu(['Ver Pessoas cadastradas', 
              'Cadastrar nova pessoa', 
              'Sair do Sistema'])
    if r == 1:
        cab('Opção 1')
    elif r == 2:
        cab('Opção 2')
    elif r == 3:
        cab('Saindo do sistema... Até Logo!')
        break    
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
