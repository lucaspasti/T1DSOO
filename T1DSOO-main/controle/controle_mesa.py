from entidade.mesa import Mesa
from limite.tela_mesa import TelaMesa

class ControladorMesa():

    def __init__(self):
        self.__mesas = []
        self.__tela_mesa = TelaMesa()

    def lista_mesas(self):
        for mesa in self.__mesas:
            self.__tela_mesa.mostra_mesa({"numero": mesa.numero, "lugares": mesa.lugares, "ocupada": mesa.ocupada})

    def incluir_mesa(self):
        dados_mesa = self.__tela_mesa.pega_dados_mesa()
        mesa = Mesa(dados_mesa["numero"], dados_mesa["lugares"], dados_mesa["status"])
        self.__mesas.append(mesa)

    def mudar_status(self):

        status_mesa = Mesa(dados_mesa["status"])

        if status_mesa is not None:

            if status_mesa == True:

                novo_status = False
            else:
                novo_status = True

            self.__ocupada = novo_status

    def alterar_mesa(self):
        self.lista_mesas()
        numero_mesa = self.__tela_mesa.seleciona_mesa()
        self.__mesa = self.__seleciona_mesa(numero_mesa)


    if (numero_mesa is not None):
        novos_dados_mesa = self.__tela_mesa.pega_dados_mesa()
        mesa.numero = novos_dados_mesa["numero"]
        mesa.lugares = novos_dados_mesa["lugares"]
        mesa.ocupada = novos_dados_mesa["status"]
        self.lista_clientes()
    else:
        self.__tela_mesa.mostra_mensagem("Mesa inválida.")
