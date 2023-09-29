from funções import fun

def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} Criado com sucesso!')    


def lerArquivo(nome):
    try: 
        with open(nome, 'rt') as a:
            fun.cab('PESSOAS CADASTRADAS')
            for linha in a:
                dado = linha.split(':')
                nome = dado[0]
                idade = dado[1].strip()
                print(f'{nome:<30}{idade:>3} Anos')
    except FileNotFoundError:
        print(f'O arquivo {nome} não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
       a = open(arquivo, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}:{idade}\n')
        except:
            print('Houve um erro na Digitação dos dados!')
        else:
            print(f'\033[32mNovo registro de {nome} adicionado com Sucesso!.\033[m')
            a.close()
    