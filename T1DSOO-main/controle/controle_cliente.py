from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente

class ControladorCliente():

    def __int__(self, controlador_cliente):
        self.__clientes = []
        self.__tela_cliente = TelaCliente()

    def pega_cliente_por_cpf(self, cpf: int):
        for cliente in self.__clientes:
            if (cliente.cpf == cpf):
                return cliente
        return None

    def lista_clientes(self):
        for cliente in self.__clientes:
            self.__tela_cliente.mostra_cliente({"nome": cliente.nome, "telefone": cliente.telefone, "cpf": cliente.cpf})

    def incluir_amigo(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        cliente = Cliente(dados_cliente["nome"], dados_cliente["telefone"], dados_cliente["cpf"])
        self.__clientes.append(cliente)

    def alterar_cliente(self):
        self.lista_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        self.__cliente = self.pega_cliente_por_cpf(cpf_cliente)

    if (cliente is not None):
        novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
        cliente.nome = novos_dados_cliente["nome"]
        cliente.telefone = novos_dados_cliente["telefone"]
        cliente.cpf = novos_dados_cliente["cpf"]
        self.lista_clientes()
    else:
        self.__tela_cliente.mostra_mensagem("Cliente inválido.")