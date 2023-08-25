d = float(input('\033[33mQual a atual cotação do dólar? \033[m'))
r = float(input('\033[33mQuantos reais você deseja converter? \033[m'))
cot = r/d
print(f'\033[33mVocê conseguirá comprar cerca de\033[m \033[32m{cot:.2f}\033[m \033[33mdólares\033[m')