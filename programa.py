from funcoes import *

cartela = {
    "regra_simples": {i: 0 for i in range(1, 7)},
    "regra_avancada": {
        "sem_combinacao": 0,
        "quadra": 0,
        "full_house": 0,
        "sequencia_baixa": 0,
        "sequencia_alta": 0,
        "cincoiguais": 0
    }
}

for  in range(12):
    dados = rolar_dados(5)
    print("Dados rolados:", dados)
    print("Escolha uma categoria:")
    categoria = input()

    cartela = faz_jogada(dados, categoria, cartela)

print("Cartela final:", cartela)