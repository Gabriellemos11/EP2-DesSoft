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

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-" * 25)
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02d} |")
        else:
            print(f"| {i}: {filler}|    |")
    for chave in cartela['regra_avancada']:
        filler = " " * (15 - len(str(chave)))
        if cartela['regra_avancada'][chave] != -1:
            print(f"| {chave}: {filler}| {cartela['regra_avancada'][chave]:02d} |")
        else:
            print(f"| {chave}: {filler}|    |")
    print("-" * 25)

def pontuacao_total(cartela):
    total = 0
    soma_simples = 0
    for valor in cartela["regra_simples"].values():
        if valor != -1:
            total += valor
            soma_simples += valor
    for valor in cartela["regra_avancada"].values():
        if valor != -1:
            total += valor
    if soma_simples >= 63:
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
        print("Digite:")
        print("1 - Guardar dado")
        print("2 - Remover dado do estoque")
        print("3 - Rerrolar dados")
        print("4 - Ver cartela")
        print("0 - Marcar pontuação")

        opcao = input()

        if opcao == "1":
            print("Índice do dado a guardar (0 a N):")
            idx = int(input())
            if 0 <= idx < len(dados_rolados):
                dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, idx)

        elif opcao == "2":
            print("Índice do dado a remover (0 a N):")
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
            print("Digite a categoria desejada:")
            categoria = input()

            if categoria in ['1', '2', '3', '4', '5', '6']:
                if cartela["regra_simples"][int(categoria)] != -1:
                    print("Essa categoria já foi usada.")
                else:
                    todos_dados = dados_rolados + dados_guardados
                    cartela = faz_jogada(todos_dados, categoria, cartela)
                    break
            elif categoria in cartela["regra_avancada"]:
                if cartela["regra_avancada"][categoria] != -1:
                    print("Essa categoria já foi usada.")
                else:
                    todos_dados = dados_rolados + dados_guardados
                    cartela = faz_jogada(todos_dados, categoria, cartela)
                    break
            else:
                print("Categoria inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente de novo.")

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao_total(cartela)}")