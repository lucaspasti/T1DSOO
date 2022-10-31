class TelaMesa():

    def tela_opcoes(self):
        print("----- Mesa -----")
        print("Escolha a opção:")
        print("1 - Checar status")
        print("2 - Mudar status")
        print("3 - Adicionar mesa")
        print("4 - Remover mesa")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))

        return opcao


    def pega_dados_mesa(self):
        numero = input("numero: ")
        lugares = input("lugares: ")
        ocupada = input("status: ")

        return {"numero": numero, "lugares": lugares, "status": ocupada}

    def mostra_mesa(self, dados_mesa):
        print("Numero da mesa: ", dados_mesa["numero"])
        print("Numero de lugares: ", dados_mesa["lugares"])
        print("Status da mesa: ", dados_mesa["status"])
        print("\n")

    def seleciona_mesa(self):
        numero = input("Numero da mesa que quer selecionar: ")
        return numero

    def mostra_mensagem(self, msg):
        print(msg)