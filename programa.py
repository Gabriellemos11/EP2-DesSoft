
from funcoes import *

cartela = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

rodada = 0
combinacoes = []

imprime_cartela(cartela)

while rodada < 12:
    dados_no_estoque = []
    dados = rolar_dados(5 - len(dados_no_estoque))

    print('Dados rolados: {}'.format(dados))
    print('Dados guardados: {}'.format(dados_no_estoque))

    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para finalizar a rodada.")
    while True:
        opcao = input('> ')

        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input('> '))
            dados, dados_no_estoque = guardar_dado(dados, dados_no_estoque, indice)
            print('Dados rolados: {}'.format(dados))
            print('Dados guardados: {}'.format(dados_no_estoque))

        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input('> '))
            dados, dados_no_estoque = remover_dado(dados, dados_no_estoque, indice)
            print('Dados rolados: {}'.format(dados))
            print('Dados guardados: {}'.format(dados_no_estoque))

        elif opcao == '3':
            dados = rolar_dados(5 - len(dados_no_estoque))
            print('Dados rerrolados: {}'.format(dados))

        elif opcao == '4':
            imprime_cartela(cartela)

        elif opcao == '0':
            break

    faz_jogada(dados + dados_no_estoque, cartela)
    rodada += 1

pontuacao_total = calcula_pontuacao(cartela)
print("Pontuação total: {}".format(pontuacao_total))
