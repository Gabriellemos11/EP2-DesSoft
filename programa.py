from funcoes import (
    imprime_cartela,
    rolar_dados,
    guardar_dado,
    remover_dado,
    calcula_pontos_regra_simples,
    calcula_pontos_soma,
    calcula_pontos_sequencia_baixa,
    calcula_pontos_sequencia_alta,
    calcula_pontos_full_house,
    calcula_pontos_quadra,
    calcula_pontos_quina,
    calcula_pontos_regra_avancada,
    faz_jogada
)

cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

categorias_usadas = []
todas_categorias = ['1', '2', '3', '4', '5', '6', 'sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']

imprime_cartela(cartela)

for _ in range(12):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    print('Dados rolados:', dados_rolados)
    print('Dados guardados:', dados_guardados)
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    acao = input(">")

    while acao != '0':
        if acao == '1':
            print("Digite o índice do dado a ser guardado (0 a {}):".format(len(dados_rolados) - 1))
            idx = int(input(">"))
            while idx >= len(dados_rolados):
                print("Índice inválido. Digite novamente:")
                idx = int(input(">"))
            resultado = guardar_dado(dados_rolados, dados_guardados, idx)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

        elif acao == '2':
            print("Digite o índice do dado a ser removido (0 a {}):".format(len(dados_guardados) - 1))
            idx = int(input(">"))
            while idx >= len(dados_guardados):
                print("Índice inválido. Digite novamente:")
                idx = int(input(">"))
            resultado = remover_dado(dados_rolados, dados_guardados, idx)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

        elif acao == '3':
            if rerrolagens < 2:
                rerrolagens += 1
                dados_rolados = rolar_dados(len(dados_rolados))
            else:
                print("Você já usou todas as rerrolagens.")

        elif acao == '4':
            imprime_cartela(cartela)

        else:
            print("Opção inválida.")

        print('Dados rolados:', dados_rolados)
        print('Dados guardados:', dados_guardados)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        acao = input(">")

    print("Digite a combinação desejada:")
    categoria = input(">")
    while categoria in categorias_usadas or categoria not in todas_categorias:
        if categoria in categorias_usadas:
            print("Essa combinação já foi utilizada.")
        else:
            print("Combinação inválida. Tente novamente.")
        categoria = input(">")

    categorias_usadas.append(categoria)
    todos_os_dados = dados_rolados + dados_guardados
    cartela = faz_jogada(todos_os_dados, categoria, cartela)

imprime_cartela(cartela)

pontuacao_total = 0
for tipo in cartela:
    for valor in cartela[tipo].values():
        if valor != -1:
            pontuacao_total += valor

bonus = sum(cartela['regra_simples'][n] for n in range(1, 7) if cartela['regra_simples'][n] != -1)
if bonus >= 63:
    pontuacao_total += 35

print("Pontuação total:", str(pontuacao_total))