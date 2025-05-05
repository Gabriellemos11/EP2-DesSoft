from funcoes import *

pontuacoes = {
    '1': None,
    '2': None,
    '3': None,
    '4': None,
    '5': None,
    '6': None,
    'sem_combinacao': None,
    'quadra': None,
    'full_house': None,
    'sequencia_baixa': None,
    'sequencia_alta': None,
    'cinco_iguais': None
}

for _ in range(12):
    dados_guardados = []
    dados_rolados = rolar_dados([])
    print(f'Dados rolados: {dados_rolados}')
    print(f'Dados guardados: {dados_guardados}')

    while True:
        acao = int(input('Digite 1 para guardar um dado, 2 para remover um dado, 0 para parar: '))
        if acao == 0:
            break
        if acao == 1:
            indice = int(input('Digite o índice do dado a ser guardado (0 a {}): '.format(len(dados_rolados) - 1)))
            dado = dados_rolados.pop(indice)
            dados_guardados.append(dado)
        elif acao == 2:
            indice = int(input('Digite o índice do dado a ser removido (0 a {}): '.format(len(dados_guardados) - 1)))
            dados_guardados.pop(indice)

        dados_rolados = rolar_dados(dados_rolados)
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')

    combinacao = input('Digite a combinação desejada: ')
    pontos = calcula_pontuacao(combinacao, dados_guardados)
    pontuacoes[combinacao] = pontos

# Impressão da cartela de pontos
print('Cartela de Pontos:')
print('-------------------------')
for chave in ['1', '2', '3', '4', '5', '6', 'sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']:
    valor = pontuacoes[chave]
    if valor is None:
        valor_str = '   '
    else:
        valor_str = str(valor).zfill(2)
    print(f'| {chave + ":":<16}| {valor_str} |')
print('-------------------------')

# Soma dos pontos
soma_simples = 0
for i in range(1, 7):
    if pontuacoes[str(i)] is not None:
        soma_simples += pontuacoes[str(i)]

soma_total = 0
for valor in pontuacoes.values():
    if valor is not None:
        soma_total += valor

if soma_simples >= 63:
    soma_total += 35

print(f'Pontuação total: {soma_total}')
