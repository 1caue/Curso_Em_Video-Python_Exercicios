def leiad(msg):
    val = False
    while not val:
        ent = str(input(msg)).replace(',' , '.').strip()
        if ent.isalpha() or ent == '':
            print(f'\033[31mErro!:\033[m \"{ent}\" \033[31mè um preço inválido\033[m')
        else:
            val = True
            return float(ent)
        
