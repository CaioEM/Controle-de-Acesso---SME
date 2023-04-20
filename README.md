# Controle-de-Acesso---SME
listaPedestres = ['caio','clecio','tatiane']
listaVeiculos = ['dtx9c47', 'cxt5190']


def menu():
    while True:
        print("\n\t\tSISTEMA DE CONTROLE - SME\n"
              "\t\t1 - Consultar Pedestre\n"
              "\t\t2 - Consultar Veículo\n"
              "\t\t3 - Consultar Ramal\n"
              "\t\t4 - Consultar Histórico")
        opcao = int(input(">>"))
        if opcao == 1:
            print("Você escolheu a opção 1")
            consultarPedestres()
        elif opcao == 2:
            print("Você escolheu a opção 2")
            consultarVeiculos()
        elif opcao == 3:
            print("Você escolheu a opção 3")
            break
        elif opcao == 4:
            print("Você escolheu a opção 4")
            break
        else:
            print("Opção inválida!")
            continue

def consultarPedestres():
    print("TELA CONSULTAR PEDESTRE")
    nomes = input("Digite o nome para consultar:")
    for nome in listaPedestres:
        if nomes == nome:
            print("Pessoa encontrada!\n"
                  "Entrada registrada com sucesso...")
            break
        else:
            print("Pessoa não cadastrada")
            while True:
                try:
                    escolha = input("Escreva:\n Y cadastra\n N encerra\n>>")
                    if escolha.upper() == 'Y':
                        print("Você acessou o menu de cadastro")
                        break
                    elif escolha.upper() == 'N':
                        print("Encerrando...")
                        break
                except ValueError:
                    print("Opção inválida")
                    continue


def consultarVeiculos():
    print("TELA CONSULTAR VEÍCULOS")
    veiculos = input("Entre com a placa do veículo: ")
    for veiculo in listaVeiculos:
        if veiculos == veiculo:
            print("Veículo encontrado!\n"
                  "Entrada registrada com sucesso...")
        else:
            print("Veículo não cadastrado!")
            while True:
                try:
                    escolha = input("Escreva:\n Y cadastra\n N encerra\n>>")
                    if escolha.upper() == 'Y':
                        print("Você acessou o menu de cadastro")
                        break
                    elif escolha.upper() == 'N':
                        print("Encerrando...")
                        break
                except ValueError:
                    print("Opção inválida")
                    continue

menu()
