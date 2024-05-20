while True:
        valor_1 = float(input('Digite o primeiro número: '))
        valor_2 = float(input('Digite o segundo número: '))

        print("\nMenu:")
        print("1 - Somar")
        print("2 - Multiplicar")
        print("3 - Dividir")
        print("4 - Subtrair")
        print("5 - Novos números")
        print("6 - Sair do Programa")


        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print("Resultado da soma:", valor_1 + valor_2)
        elif opcao == 2:
            print("Resultado da multiplicação:", valor_1 * valor_2)
        elif opcao == 3:
            if valor_2 != 0:
                print("Resultado da divisão:", valor_1 / valor_2)
            else:
                print("Erro: divisão por zero")
        elif opcao == 4:
            print("Resultado da subtração:", valor_1 - valor_2)
        elif opcao == 5:
            continue
        elif opcao == 6:
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        