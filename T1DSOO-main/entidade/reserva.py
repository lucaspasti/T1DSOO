from mesa import Mesa
from cliente import Cliente

class Reserva:

    def __int__(self, mesa:Mesa, qtd_pessoas:int, cliente:Cliente):
        self.__mesa = mesa
        self.__qtd_pessoas = qtd_pessoas
        self.__cliente = cliente

    @property
    def mesa(self):
        return self.__mesa

    @property
    def qtd_pessoas(self):
        return self.__qtd_pessoas

    @property
    def cliente(self):
        return self.__cliente

    @mesa.setter
    def mesa (self, mesa):
        self.__mesa = mesa

    @qtd_pessoas.setter
    def qtd_pessoas(self, qtd_pessoas):
        self.__qtd_pessoas = qtd_pessoas

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente