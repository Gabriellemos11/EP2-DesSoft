from funcoes import *
import random

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        valor = cartela['regra_simples'][i]
        if valor != -1:
            print(f"| {i}: {filler}| {valor:>2} |")
        else:
            print(f"| {i}: {filler}|    |")
    for chave in ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']:
        filler = " " * (15 - len(str(chave)))
        valor = cartela['regra_avancada'][chave]
        if valor != -1:
            print(f"| {chave}: {filler}| {valor:>2} |")
        else:
            print(f"| {chave}: {filler}|    |")
    print("-"*25)

# Inicializa cartela
cartela = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

for rodada in range(12):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    while True:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        try:
            acao = int(input())
        except ValueError:
            print("Opção inválida. Tente novamente.")
            continue

        if acao == 1:
            print("Digite o índice do dado a ser guardado (0 a 4):")
            try:
                idx = int(input())
                if 0 <= idx < len(dados_rolados):
                    dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, idx)
                else:
                    print("Índice inválido.")
            except:
                print("Índice inválido.")
        elif acao == 2:
            print("Digite o índice do dado a ser removido (0 a 4):")
            try:
                idx = int(input())
                if 0 <= idx < len(dados_guardados):
                    dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, idx)
                else:
                    print("Índice inválido.")
            except:
                print("Índice inválido.")
        elif acao == 3:
            if rerrolagens < 2:
                rerrolagens += 1
                dados_rolados = rolar_dados(len(dados_rolados))
            else:
                print("Você já usou todas as rerrolagens.")
        elif acao == 4:
            imprime_cartela(cartela)
        elif acao == 0:
            print("Digite a combinação desejada:")
            categoria = input()

            categorias_validas = [str(i) for i in range(1, 7)] + [
                'sem_combinacao', 'quadra', 'full_house',
                'sequencia_baixa', 'sequencia_alta', 'cinco_iguais'
            ]

            if categoria not in categorias_validas:
                print("Combinação inválida. Tente novamente.")
                continue

            if categoria in cartela['regra_simples'] and cartela['regra_simples'][int(categoria)] != -1:
                print("Essa combinação já foi utilizada.")
                continue
            elif categoria in cartela['regra_avancada'] and cartela['regra_avancada'][categoria] != -1:
                print("Essa combinação já foi utilizada.")
                continue

            dados_final = dados_rolados + dados_guardados
            cartela = faz_jogada(dados_final, categoria, cartela)
            break
        else:
            print("Opção inválida. Tente novamente.")

# Fim do jogo
imprime_cartela(cartela)

simples = sum(p for p in cartela['regra_simples'].values() if p != -1)
bonus = 35 if simples >= 63 else 0
total = simples + sum(p for p in cartela['regra_avancada'].values() if p != -1) + bonus

print(f"Pontuação total: {total}")
