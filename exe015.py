qtdekm = float(input(f'\033[33mQuantos KMs foram percorridos com o carro alugado?\033[m  '))
dias = int(input(f'\033[33mQQuantos dias o carro foi alugado?\033[m  '))
pkm = (qtdekm*0.15)
preco = (dias*60)+pkm
print(f'\033[33mO preço a se pagar pelos com o aluguel de \033[32m{dias} \033[33mdias e \033[32m{qtdekm}KMs \033[33mrodados é de \033[32mR${preco:.2f}\033[m')