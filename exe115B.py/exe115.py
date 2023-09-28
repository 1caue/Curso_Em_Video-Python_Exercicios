from funções import fun
from funções import arq
from time import sleep

arquivo = "cursoemvideo.txt"

if not arq.arquivoExiste(arquivo):
    arq.criarArquivo(arquivo)

while True:
    resp = fun.menu(['Ver Pessoas cadastradas', 
              'Cadastrar Novas Pessoas', 
              'Sair do Sistema'])
    if resp == 1:
        # Opção de listar o conteudi de um arquivo!
        arq.lerArquivo(arquivo)
    elif resp == 2:
        # Opção de cadastrar uma nova pessoa.
        fun.cab('Opção 2')
    elif resp == 3:
        # Opção de sair do sistema.
        sleep(1)
        fun.cab('Saindo do sistema... Até Logo!')
        sleep(2)
        break    
    else:
        # Digitou uma opção errada no menu
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
