n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print(f'Tirando {n1} e {n2}, a média é {m} \nO aluno está REPROVADO')
elif m > 5 and m < 6.9:
    print(f'Tirando {n1} e {n2}, a média é {m} \nO aluno está de RECUPERAÇÃO')
elif m > 7:
    print(f'Tirando {n1} e {n2}, a média é {m} \nO aluno está APROVADO')