an = int(input('Ano de Nascimrnto: '))
id = 2023 - an
if id <= 9:
    print(f'O atleta tem {id} anos. \nClassificação MIRIM')
elif id <= 14:
    print(f'O atleta tem {id} anos. \nClassificação INFANTIL')
elif id <= 19:
    print(f'O atlera tem {id} anos. \nClassificaçao JUMIOR')
elif id <= 25:
    print(f'O atleta tem {id} anos. \nClassificação SÊNIOR')
else:
    print(f'O atleta tem {id} anos. \nClassificação MASTER')
