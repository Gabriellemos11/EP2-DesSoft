from funcoes import rolar_dados, guardar_dado, remover_dado, calcula_pontuacao

if __name__ == "__main__":
    cartela = {
        "1": None, "2": None, "3": None, "4": None, "5": None, "6": None,
        "sem_combinacao": None, "quadra": None, "full_house": None,
        "sequencia_baixa": None, "sequencia_alta": None, "cinco_iguais": None
    }

    dados_guardados = []
    dados_rolados = rolar_dados(5)
    print("Cartela de Pontos:")
    print("-------------------------")
    for k in cartela:
        print(f"| {k:<15} | {cartela[k] if cartela[k] is not None else '':>2} |")
    print("-------------------------")
    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")

    while True:
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para encerrar a rodada")
        comando = input("Escolha: ")
        if comando == "1":
            pos = int(input("Qual a posição do dado que deseja guardar? (0 a n): "))
            dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, pos)
        elif comando == "2":
            pos = int(input("Qual a posição do dado que deseja remover? (0 a n): "))
            dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, pos)
        elif comando == "3":
            break
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")

    dados_finais = dados_guardados + dados_rolados
    categoria = input("Digite uma categoria: ")
    pontuacao = calcula_pontuacao(dados_finais, categoria)
    cartela[categoria] = pontuacao

    print("Cartela de Pontos:")
    print("-------------------------")
    for k in cartela:
        print(f"| {k:<15} | {cartela[k] if cartela[k] is not None else '':>2} |")
    print("-------------------------")