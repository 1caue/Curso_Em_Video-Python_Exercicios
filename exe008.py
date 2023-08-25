n = float(input('\033[33mDigite uma medida em metros:  \033[m'))
cm = n/0.01
mm = n/0.001
km = n/1000
print(f'\033[31m{n}\033[mm \033[32m{cm}\033[mcm \033[34m{mm}\033[mmm \033[35m{km}\033[mkm')
