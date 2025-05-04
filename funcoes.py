import random

def rolar_dados(qtd_dados):
    resultado = []
    for _ in range(qtd_dados):
        resultado.append(random.randint(1, 6))
    return resultado

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_no_estoque.append(dado_para_guardar)
    dados_rolados.remove(dado_para_guardar)
    return [dados_rolados, dados_no_estoque]
