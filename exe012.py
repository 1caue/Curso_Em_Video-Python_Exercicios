p = float(input('\033[33mQual o preço do produto? \033[m'))
x = int(input('\033[33mDe quanto será o desconto? \033[m'))
d = (p/100) * x
v = p-d
print(f'\033[33mO produto que custava \033[32mR${p:.2f}, \033[33mcom \033[32m{x}% \033[33mde desconto vai custar \033[32mR${v:.2f}\033[m')