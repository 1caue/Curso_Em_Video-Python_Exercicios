s = float(input('\033[33mQual é o sálario do funcionário? \033[m \033[32mR$'))
a = s + (s * 0.15)
print(f'\033[33mUm funcionário que ganhava \033[32mR${s:.2f}\033[33m, com \033[33m15% \033[33mde aumento.\nPassa a receber \033[32mR${a:.2f}.')