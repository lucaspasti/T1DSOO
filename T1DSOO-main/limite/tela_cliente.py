class TelaCliente():

    def tela_opcoes(self):
        print("----- Cliente -----")
        print("Escolha a opção:")
        print("1 - Incluir cliente")
        print("2 - Alterar cliente")
        print("3 - Listar cliente")
        print("4 - Excluir cliente")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))

        return opcao


    def pega_dados_cliente(self):
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        cpf = input("CPF: ")

        return {"nome": nome, "telefone": telefone, "cpf": cpf}

    def mostra_cliente(self, dados_cliente):
        print("NOME DO CLIENTE: ", dados_cliente["nome"])
        print("FONE DO CLIENTE: ", dados_cliente["telefone"])
        print("CPF DO CLIENTE: ", dados_cliente["cpf"])
        print("\n")

    def seleciona_cliente(self):
        cpf = input("CPF do cliente que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)

