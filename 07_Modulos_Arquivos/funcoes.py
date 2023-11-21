

def somar():
    print("essa é uma função de teste com nome SOMAR")
    

def multi():
    print("essa é uma função de teste com nome de MULTI")
    

def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return 1
    return -1