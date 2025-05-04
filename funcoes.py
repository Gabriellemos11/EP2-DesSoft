import random

def rolar_dados(qtd_dados):
    resultado = []
    for _ in range(qtd_dados):
        resultado.append(random.randint(1, 6))
    return resultado
