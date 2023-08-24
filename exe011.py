l = float(input('\033[1;35mDigite a largura da parede: \033[m'))
a = float(input('\033[1;35mDigite a altura da parede: \033[m'))
p = l * a 
t = p / 2.2
print(f'\033[1;35mSerá nescessário\033[m \033[1;32m{t:.2f}\033[m \033[1;35mlitros de tinta para pintar sua parede de\033[m \033[1;32m{p}m²\033[m')