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
    print("-"*25)
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        valor = cartela['regra_simples'][i]
        linha = f"| {i}:{filler}| {'   ' if valor == -1 else f'{valor:02d}'} |"
        print(linha)
    for chave, valor in cartela['regra_avancada'].items():
        filler = " " * (15 - len(str(chave)))
        linha = f"| {chave}:{filler}| {'   ' if valor == -1 else f'{valor:02d}'} |"
        print(linha)
    print("-"*25)

def pontuacao_total(cartela):
    total = 0
    simples = 0
    for v in cartela["regra_simples"].values():
        if v != -1:
            total += v
            simples += v
    for v in cartela["regra_avancada"].values():
        if v != -1:
            total += v
    if simples >= 63:
        total += 35
    return total

cartela = inicializa_cartela()
for _ in range(12):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0
    jogada_feita = False

    while not jogada_feita:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar, 2 para remover, 3 para rerrolar, 4 ver cartela, 0 marcar ponto:")

        try:
            opcao = input().strip()
        except:
            break

        if opcao == "1":
            if len(dados_rolados) > 0:
                print("Índice do dado (0 a N):")
                idx = int(input())
                if 0 <= idx < len(dados_rolados):
                    dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, idx)

        elif opcao == "2":
            if len(dados_guardados) > 0:
                print("Índice do dado (0 a N):")
                idx = int(input())
                if 0 <= idx < len(dados_guardados):
                    dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, idx)

        elif opcao == "3":
            if rerrolagens < 2:
                rerrolagens += 1
                dados_rolados = rolar_dados(len(dados_rolados))
            else:
                print("Rerrolagens esgotadas.")

        elif opcao == "4":
            imprime_cartela(cartela)

        elif opcao == "0":
            print("Digite a categoria:")
            categoria = input().strip()
            todos = dados_rolados + dados_guardados

            if categoria in ['1','2','3','4','5','6']:
                if cartela['regra_simples'][int(categoria)] == -1:
                    cartela = faz_jogada(todos, categoria, cartela)
                    jogada_feita = True
                else:
                    print("Já usada.")
            elif categoria in cartela['regra_avancada']:
                if cartela['regra_avancada'][categoria] == -1:
                    cartela = faz_jogada(todos, categoria, cartela)
                    jogada_feita = True
                else:
                    print("Já usada.")
            else:
                print("Categoria inválida.")
        else:
            print("Opção inválida.")

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao_total(cartela)}")
