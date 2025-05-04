import random

def rolar_dados(qtd_dados):
    resultado = []
    for _ in range(qtd_dados):
        resultado.append(random.randint(1, 6))
    return resultado

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado = dados_rolados[dado_para_guardar]
    dados_no_estoque.append(dado)
    dados_rolados.pop(dado_para_guardar)
    return [dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado = dados_no_estoque[dado_para_remover]
    dados_rolados.append(dado)
    dados_no_estoque.pop(dado_para_remover)
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(dados):
    resultado = {i: 0 for i in range(1, 7)}
    for numero in dados:
        if numero in resultado:
            resultado[numero] += numero
    return resultado
