# Def
def voto(a=0):
    import datetime
    s = datetime.date.today().year
    i = s - a
    if i < 16:
        print(f'Com {i} anos: \033[31mNÃO VOTA\033[m.')
    elif 16 <= i < 18 or i > 70:
        print(f'Com {i} anos: \033[32mVOTO OPCIOMAL\033[m.')
    else:
        print(f'Com {i} anos: \033[33mVOTO OBRIGATÓRIO\033[m.')


# Programa principal
print('\033[33m-\033[m' * 35)
voto(int(input('Em que ano você nasceu?: ')))

