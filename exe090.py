l = {}
l['nome'] = str(input('Nome: '))
l['media'] = float(input(f'Média de {l["nome"]}: '))
print('-=' * 30)
print(f' - nome é igual a {l["nome"]}')
print(f' - média igual a {l["media"]}')
if l['media'] >= 7:
    print(' - situação é igual a aprovado')
elif 5 <= l['media' ] < 7:
    print(' - A situação é igual a Recuperação')
else:
    print(' - Aluno Reprovado')
