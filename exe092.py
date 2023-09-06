from datetime import datetime
cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
cadastro['Idade'] = datetime.now().year - nasc
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['CTPS'] != 0: 
    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Sálario'] = float(input('Sálario R$'))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Contratação'] + 35) - datetime.now().year)
print('\033[33m-=\033[m' * 30)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}.')

