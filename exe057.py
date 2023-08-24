n = str(input('Informe o seu sexo [M/F]: ')).upper()
while n not in 'MmFf': 
    n = str(input('Dados Inválidos. Por favor, informe seu sexo: '))
print(f'Sexo \033[32m{n}\033[m registrado com suceesso')
