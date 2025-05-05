import random
from collections import Counter

def rolar_dados(qtd_dados):
    return [random.randint(1, 6) for _ in range(qtd_dados)]

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

def calcula_pontuacao(dados, categoria):
    contagem = Counter(dados)
    if categoria in ["1", "2", "3", "4", "5", "6"]:
        numero = int(categoria)
        return dados.count(numero) * numero
    elif categoria == "sem_combinacao":
        return sum(dados)
    elif categoria == "quadra":
        for numero, qtd in contagem.items():
            if qtd >= 4:
                return sum(dados)
        return 0
    elif categoria == "full_house":
        if sorted(contagem.values()) == [2, 3]:
            return 25
        return 0
    elif categoria == "sequencia_baixa":
        if set([1,2,3,4]).issubset(dados) or            set([2,3,4,5]).issubset(dados) or            set([3,4,5,6]).issubset(dados):
            return 30
        return 0
    elif categoria == "sequencia_alta":
        if set([1,2,3,4,5]).issubset(dados) or set([2,3,4,5,6]).issubset(dados):
            return 40
        return 0
    elif categoria == "cinco_iguais":
        if any(qtd == 5 for qtd in contagem.values()):
            return 50
        return 0
    else:
        return 0