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
    conjunto = set(dados)
    sequencias_altas = [
        {1, 2, 3, 4, 5},
        {2, 3, 4, 5, 6}
    ]
    for sequencia in sequencias_altas:
        if sequencia.issubset(conjunto):
            return 30
    return 0

def calcula_pontos_full_house(dados):
    contagens = {}
    for valor in dados:
        contagens[valor] = contagens.get(valor, 0) + 1

    if len(contagens) != 2:
        return 0

    valores = list(contagens.values())
    if 3 in valores and 2 in valores:
        total = 0
        for numero in dados:
            total += numero
        return total

    return 0

def calcula_pontos_quadra(dados):
    contagens = {}
    for valor in dados:
        contagens[valor] = contagens.get(valor, 0) + 1

    for quantidade in contagens.values():
        if quantidade >= 4:
            total = 0
            for numero in dados:
                total += numero
            return total

    return 0

def calcula_pontos_quina(dados):
    contagens = {}
    for valor in dados:
        contagens[valor] = contagens.get(valor, 0) + 1

    for quantidade in contagens.values():
        if quantidade >= 5:
            return 50

    return 0

def calcula_pontos_regra_avancada(dados):
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }

def faz_jogada(dados, categoria, cartela_de_pontos):
    if categoria in cartela_de_pontos["regra_simples"]:
        cartela_de_pontos["regra_simples"][categoria] = calcula_pontos_regra_simples(dados)
    else:
        cartela_de_pontos["regra_avancada"][categoria] = calcula_pontos_regra_avancada(dados)
    return cartela_de_pontos
