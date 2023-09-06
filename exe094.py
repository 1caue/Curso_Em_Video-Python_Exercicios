g = []
p = {}
som = media = 0
while True:
    p.clear()
    p['nome'] = str(input('Nome: '))
    while True: 
        p['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if p['sexo'] in 'MF':
            break
        print('Erro!, por favor digite apenas M ou F')
    p['idade'] = int(input('Idade: '))
    som += p['idade']
    g.append(p.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N.' )
    if r == 'N':
        break
print('-=' * 30)
# ↟ Leitura de dados ↟ 
# A ↡
print(f' - Ao todo temos {len(g)} pessoas cadastradas')
media = som / len(g)
# B ↡
print(f' - A média de idade é de {media:5.1f} anos')
# C ↡
print(' - As mulheres cadastradas foram', end='')
for p in g:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end=' ')
print('\n')
# D ↡
print('Lista das pessoas que estão acima da média: ', end='')
for p in g:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRANDO >>')
