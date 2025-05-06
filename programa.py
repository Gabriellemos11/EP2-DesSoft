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
            dados = rerrolar(dados, 5 - len(dados_no_estoque))
            print('Dados rerrolados: {}'.format(dados))

        elif opcao == '4':
            imprime_cartela(cartela)

        elif opcao == '0':
            dados = dados_no_estoque + dados  # juntar todos os dados
            combinacao = faz_jogada(dados)
            combinacoes.append(combinacao)
            cartela, pontos = pontuar(cartela, combinacao)
            print('Combinação escolhida:', combinacao)
            print('Pontuação da jogada:', pontos)
            rodada += 1
            break  # sai do while interno e volta para a próxima rodada

        else:
            print("Opção inválida. Tente novamente.")
