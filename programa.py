from funcoes import *

def inicializa_cartela():
    return {
        "regra_simples": {i: -1 for i in range(1, 7)},
        "regra_avancada": {
            "sem_combinacao": -1,
            "quadra": -1,
            "full_house": -1,
            "sequencia_baixa": -1,
            "sequencia_alta": -1,
            "cinco_iguais": -1
        }
    }

def pontuacao_total(cartela):
    total = 0
    simples = 0
    for valor in cartela["regra_simples"].values():
        if valor != -1:
            total += valor
            simples += valor
    for valor in cartela["regra_avancada"].values():
        if valor != -1:
            total += valor
    if simples >= 63:
        total += 35
    return total

cartela = inicializa_cartela()
rodadas = 12

for _ in range(rodadas):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    while True:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        opcao = input()
        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            idx = int(input())
            if 0 <= idx < len(dados_rolados):
                dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, idx)

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            idx = int(input())
            if 0 <= idx < len(dados_guardados):
                dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, idx)

        elif opcao == "3":
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                rerrolagens += 1
                dados_rolados = rolar_dados(len(dados_rolados))

        elif opcao == "4":
            imprime_cartela(cartela)

        elif opcao == "0":
            print("Digite a combinação desejada:")
            categoria = input()
            if categoria in ['1', '2', '3', '4', '5', '6']:
                cat_int = int(categoria)
                if cartela["regra_simples"][cat_int] != -1:
                    print("Essa combinação já foi utilizada.")
                else:
                    todos_dados = dados_rolados + dados_guardados
                    cartela = faz_jogada(todos_dados, categoria, cartela)
                    break
            elif categoria in cartela["regra_avancada"]:
                if cartela["regra_avancada"][categoria] != -1:
                    print("Essa combinação já foi utilizada.")
                else:
                    todos_dados = dados_rolados + dados_guardados
                    cartela = faz_jogada(todos_dados, categoria, cartela)
                    break
            else:
                print("Combinação inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao_total(cartela)}")