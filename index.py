listaPedestres = ['caio',50148921833,'sem motivo', 'DAE', 'TI',] 
listaVeiculos = ['cwg2145']
listaRamais = ['clecio',7055,'DAE']
listaHistorico = ['caio',1394894,7055,'DAE','18/04/2023','10:40', 'NAED Sul', 'SME-Ateneu', 'Pedestre','NA']
"""FUNÇÃO INICIAL PARA CONSULTAR/CADASTRAR VEICULOS E PEDESTRES"""
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
            consultaRamais() 
        elif opcao == 4: 
            print("Você escolheu a opção 4") 
            consultaHistorico()
        else: 
            print("Opção inválida!") 
            continue
"""TÉRMINO FUNÇÃO CONSULTA/CADASTRO"""

"""INICIO DA FUNÇÃO DE CONSULTAR PEDESTRE, ELA VERIFICA SE O NOME DIGITADO ESTA REGISTRADO NA LISTA(BD) E RETORNA O RESULTADO"""
def consultarPedestres(): 
    print("TELA CONSULTAR PEDESTRE")
    nomes = input("Digite o nome para consultar:")
    for nome in listaPedestres: 
        if nomes == nome:
            print("Pessoa encontrada!\n"
                  "Entrada registrada com sucesso...") 
            break
        else:
            cadastrarPedestres()
            break
                 
"""TÉRMINO DA FUNÇÃO CONSULTAR PEDESTRE"""

"""INICIO DA FUNÇÃO DE CADASTRAR PEDESTRE, ELA SOLICITA OS DADOS QUE SERÃO UTILIZADOS PARA REALIZAR O CADASTRO E INFORMA SE OBTEVE SUCESSO"""
def cadastrarPedestres():
    while True:
        print("TELA CADASTRAR PEDESTRES")
        pedestre = input("NOME: ")
        listaPedestres.append(pedestre)
        cpf = int(input("CPF/MATRÍCULA: "))
        listaPedestres.append(cpf)
        motivo = input("MOTIVO DA VISITA: ")
        listaPedestres.append(motivo)
        departamento = input("DEPARTAMENTO A VISITAR: ")
        listaPedestres.append(departamento)
        origem = input("ORIGEM VISITANTE: ")
        listaPedestres.append(origem)
        print(listaPedestres)
        listaHistorico.append(pedestre)
        listaHistorico.append(cpf)
        listaHistorico.append(motivo)
        listaHistorico.append(departamento)
        listaHistorico.append(origem)
        #'caio',1394894,7055,'DAE','18/04/2023','10:40', 'NAED Sul', 'SME-Ateneu', 'Pedestre','NA'
        print("Pessoa registrada com sucesso!")
        break
"""TÉRMINO DA FUNÇÃO CONSULTAR PEDESTRE"""


"""INICIO DA FUNÇÃO DE CONSULTAR VEICULOS, ELA SOLICITA A PLACA E VERIFICA SE ESTA REGISTRADA NA LISTA(BD) E RETORNA O RESULTADO"""
def consultarVeiculos():
    print("TELA CONSULTAR VEÍCULOS") 
    veiculos = input("Entre com a placa do veículo: ") 
    for veiculo in listaVeiculos: 
        if veiculos == veiculo: 
            print("Veículo encontrado!\n" "Entrada registrada com sucesso...") 
        else: 
            print("Veículo não cadastrado!") 
            while True: 
                try: 
                    escolha = input("Escreva:\n S para cadastrar\n N para encerrar o programa\n>>") 
                    if escolha.upper() == 'S': 
                        print("Você acessou o menu de cadastro") 
                        cadastrarVeiculos()
                    elif escolha.upper() == 'N': 
                        print("Encerrando...") 
                        break 
                except ValueError: 
                    print("Opção inválida")
                    continue
"""TÉRMINO DA FUNÇÃO CONSULTAR VEÍCULO"""

"""INICIO DA FUNÇÃO DE CADASTRAR VEÍCULO, ELA SOLICITA OS DADOS QUE SERÃO UTILIZADOS PARA REALIZAR O CADASTRO E INFORMA SE OBTEVE SUCESSO"""
def cadastrarVeiculos():
    print("TELA CADASTRAR PEDESTRES")
    condutor = input("NOME: ")
    listaVeiculos.append(condutor)
    placa = int(input("CPF/MATRÍCULA: "))
    listaVeiculos.append(placa)
    modelo = input("MODELO DO VEICULO:")
    listaVeiculos.append(modelo)
    cpf = int(input("CPF/MATRÍCULA: "))
    listaVeiculos.append(cpf)
    departamento = input("DEPARTAMENTO A VISITAR: ")
    listaVeiculos.append(departamento)
    motivo = input("MOTIVO DA VISITA: ")
    listaVeiculos.append(motivo)
    origem = input("ORIGEM VISITANTE: ")
    listaVeiculos.append(origem)
    print(listaVeiculos)
    print("Veículo registrado com sucesso!")
"""TÉRMINO DA FUNÇÃO CADASTRAR VEÍCULOS"""
    
def consultaRamais():
    print("TELA CONSULTAR RAMAIAS")
    nome = input("Digite o nome do funcionario para consultar: ")
    if nome in listaRamais:
        print("NOME  -  RAMAL  -  SETOR")
        print(listaRamais)
    else:
        print("Pessoa não encontrada")

def consultaHistorico():
    print("TELA HISTÓRICO")
    print("FUNCIONÁRIO - MATRÍCULA - RAMAL - SETOR - DATA - HORA - ORIGEM - DESTINO - TIPO ENTRADA - PLACA")
    print(listaHistorico)
menu()