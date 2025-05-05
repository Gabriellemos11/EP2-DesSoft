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

def calcula_pontos_soma(dados):
    total = 0
    for numero in dados:
        total += numero
    return total

def calcula_pontos_sequencia_baixa(dados):
    conjunto = set(dados)
    sequencias_baixas = [
        {1, 2, 3, 4},
        {2, 3, 4, 5},
        {3, 4, 5, 6}
    ]
    for sequencia in sequencias_baixas:
        if sequencia.issubset(conjunto):
            return 15
    return 0

def calcula_pontos_sequencia_alta(dados):
    if [1, 2, 3, 4, 5] in dados or [2, 3, 4, 5, 6] in dados:
        return 30
    return 0
