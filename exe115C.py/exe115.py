from funções import fun
from funções import arq
from time import sleep

arquivo = 'cadastros.txt'

if not arq.arquivoExiste(arquivo):
    arq.criarArquivo(arquivo)

while True:
    resp = fun.menu(['Ver Pessoas cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    # Opção de listar o conteudi de um arquivo!
    if resp == 1:
        sleep(0.5)
        arq.lerArquivo(arquivo)
    # Opção de cadastrar uma nova pessoa.
    elif resp == 2:
        sleep(0.5)
        fun.cab('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = fun.leiaint('Idade: ')
        arq.cadastrar(arquivo, nome, idade)
    # Opção de sair do sistema.
    elif resp == 3:
        sleep(0.5)
        fun.cab('Saindo do sistema... Até Logo!')
        break    
    # Digitou uma opção errada no menu
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
