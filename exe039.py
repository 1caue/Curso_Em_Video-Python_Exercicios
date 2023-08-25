from datetime import date
a = float(input('Ano de nascimento: '))
at = date.today().year
idade = at - a
if idade == 18:
   print('Está na hora do seu alistamento')
elif idade < 18:
    saldo = 18 - idade
    ano = saldo + at
    print(f'Quem nasceu em {a:.0f} e tem {idade:.0f} anos em {at}')
    print(f'Você terá que se alistar em {ano}')
    print(f'Ainda faltam {saldo:.0f} anos para seu alistamento')
elif idade > 18:
    saldo = idade - 18
    ano = at - saldo
    print(f'Quem nasceu em {a:.0f} tem {at - a:.0f} anos em {at}')
    print(f'Você deveria ter se alistado há {saldo:.0f} anos')
    print(f'Você deveria se alistar em {ano:.0f}')
